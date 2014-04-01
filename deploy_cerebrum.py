#!/user/bin/env python

# Use optparse because we're on old Python
from optparse import OptionParser
import string
import os


def main():
    # All instances we currently have.
    # Keys are the full name of the instance,
    # values are the shorthand "slug" used in usernames.
    all_instances = {'uio': 'uio',
                     'uia': 'uia',
                     'ofk': 'ofk',
                     'hiof': 'hiof',
                     'nmh': 'nmh',
                     'hih': 'hih',
                     'nih': 'nih',
                     'giske': 'gisk',
                     'hine': 'hine',
                     'webid': 'wid'}

    usage = "usage: %prog [options] instances"
    parser = OptionParser(usage)
    parser.add_option("-a", "--all-instances", dest="instances",
                      action="store_const", const=all_instances,
                      help="Shorthand for deploying on all instances")
    parser.add_option("--no-setup", action="store_false", dest="setup",
                      default=True, help="Do not run setup.py")
    parser.add_option("-b", "--restart-bofhd", action="store_true",
                      help="Restart bofhd")
    parser.add_option("-j", "--restart-job_runner", action="store_true",
                      help="Restart job_runner. Note: Runs --quit directly, "
                      "does not wait for jobs to finish.")
    parser.add_option("-s", "--reload-scheduled_jobs", action="store_true",
                      help="Make job_runner reload new scheduled_jobs.")
    parser.add_option("-n", "--restart-individuation", action="store_true",
                      help="Restart Individuation")
    parser.add_option("-r", "--restart-all", action="store_true",
                      help="Restart bofhd, job_runner and Individuation")
    parser.add_option(
        "--only-insert-codes", dest="makedb", action="store_const",
        const="--only-insert-codes", help="makedb.py: Make sure all "
        "code values for the current configuration of "
        "cereconf.CLASS_CONSTANTS have been inserted into the "
        "database. Does not create tables. This is the default.")
    parser.add_option("--update-codes", dest="makedb", action="store_const",
                      const="--update-codes", default="--only-insert-codes",
                      help="makedb.py: Like --only-insert-codes, but will remove"
                      " constants that exists in the database, but not in "
                      "CLASS_CONSTANTS (subject to FK constraints).")

    options, args = parser.parse_args()

    if (len(args) > 0 and parser.has_option('instances')):
        parser.error("Are you sure you meant to deploy on all instances when "
                     "you also specified instances?")

    if len(args) > 0:
        options.instances = dict((i, all_instances[i]) for i in args)

    if options.instances == None:
        parser.error("Must specify instances, either with --instances or "
                     "--all-instances")

    if (options.restart_all and (options.restart_bofhd or
                                 options.restart_job_runner or
                                 options.restart_individuation)):
        parser.error("Are you sure you meant --restart-all when you also "
                     "to restart a specific service?")

    if options.restart_all:
        options.restart_job_runner =\
            options.restart_bofhd =\
            options.restart_individuation = True

    if (options.reload_scheduled_jobs and options.restart_job_runner):
        parser.error("Are you sure you meant to restart job_runner when you "
                     "also wanted to reload its scheduled_jobs?")

    # Production MAXIMUM
    for instance in options.instances.keys():
        user = "cere%s" % options.instances[instance]

        # git pull
        print("%s: Pulling…") % instance
        os.system("ssh cerebrum-%s \"su - %s -c 'cd /cerebrum/%s/%s/src/cerebrum; "
                  "git pull'\"" % (instance, user, instance, user))

        # setup.py
        if options.setup:
            print("%s: Setting up…") % instance
            os.system("ssh cerebrum-%s \"su - %s -c "
                      "'python /cerebrum/%s/%s/src/cerebrum/setup.py install "
                      "--prefix=/cerebrum/%s/ |egrep -v \"skipping|not\"'\"" % (
                          (instance, user, instance, user, instance)))

        # makedb.py, --only-insert-codes is default
        print("%s: Making database…") % instance
        os.system("ssh cerebrum-%s \"su - %s -c 'python "
                  "/cerebrum/%s/%s/src/cerebrum/makedb.py --debug %s'\"" % (
                      (instance, user, instance, user, options.makedb)))

        # Restart services
        job_runner = "/cerebrum/%s/sbin/job_runner.py" % instance

        if options.restart_job_runner:
            print("%s: Restarting job_runner…") % instance
            os.system("ssh cerebrum-%s \"su - %s -c '%s --quit'\"" % (
                      (instance, user, job_runner)))

        if options.reload_scheduled_jobs:
            print("%s: Reloading scheduled_jobs…") % instance
            os.system("ssh cerebrum-%s \"su - %s -c '%s --reload'\"" % (
                      (instance, user, job_runner)))

        if options.restart_bofhd:
            bofhd_pid = "ps aux | grep /cerebrum/%s/sbin/bofhd.py | grep -v "\
                        "keep-running | grep -v grep | tr -s \" \" | cut -f 2 -d \" \""\
                        % instance
            print("%s: Killing bofhd…") % instance
            os.system("ssh cerebrum-%s \"su - %s -c 'kill `%s`'\"" % (
                      (instance, user, bofhd_pid)))

if __name__ == "__main__":
    main()
