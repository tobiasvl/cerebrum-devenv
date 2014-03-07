import cerebrum_path
import cereconf
from Cerebrum import Errors
from Cerebrum import Utils

db = Utils.Factory.get('Database')()
co = Utils.Factory.get('Constants')(db)
pe = Utils.Factory.get('Person')(db)
pers = Utils.Factory.get('Person')(db)
ac = Utils.Factory.get('Account')(db)

#pe.find(712347)
#pe.get_primary_account
#ac.find(2061060L)
#ac.get_names()
for person in pers.search(exclude_deceased=True):
  try:
    pe.find(person[0])
    ac.find(pe.get_primary_account())
    username = ac.get_names()[0][0]
    #for id in (705136, 712347):
    for contact in pe.list_contact_info(person[0]):
      if contact[1] == 674 and contact[2] == int(co.contact_mobile_phone):
        print "%s: %s" % (username, contact[4])
    pe.clear()
    ac.clear()
  except (Errors.NotFoundError, AttributeError):
    pe.clear()
    ac.clear()
