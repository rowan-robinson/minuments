from config import SQLALCHEMY_DATABASE_URI
from app import app, db
import os.path

with app.app_context():
    db.create_all()


    # # ITEMS ==================================================================================================

    # # 01 - RIFFA CLOCK TOWER
    # minument1 = Items(id=1,
    #                   city='RIFFA',
    #                   country='bh',
    #                   country_alttext='The flag of Bahrain.',
    #                   monument='Riffa Clock Tower',
    #                   monument_alttext='A picture of Riffa Clock Tower during the day, functioning as a placeholder.',
    #                   description='This is where an actual description of the monument would go, going into its history and such. However,  this isn\'t a real website,  so enjoy the filler text below.')
    # db.session.add(minument1)
    # db.session.commit()

    # # 02 - SIGN FOR ART
    # minument2 = Items(id=2,
    #                   city='LEEDS',
    #                   country='gb',
    #                   country_alttext='The flag of the United Kingdom.',
    #                   monument='Sign for Art',
    #                   monument_alttext='A picture of the Sign for Art during the day, functioning as a placeholder.',
    #                   description='The Wavy Bacon Statue!')
    # db.session.add(minument2)

    # # 03 - BURJ KHALIFA
    # minument3 = Items(id=3,
    #                   city='DUBAI',
    #                   country='ae',
    #                   country_alttext='The flag of the United Arab Emirates.',
    #                   monument='Burj Khalifa',
    #                   monument_alttext='A picture of the Burj Khalifa during a cloudy day, functioning as a placeholder.',
    #                   description='This is where an actual description of the monument would go, going into its history and such. However,  this isn\'t a real website,  so enjoy the filler text below.')
    # db.session.add(minument3)

    # # 04 - EIFFEL TOWER
    # minument4 = Items(id=4,
    #                   city='PARIS',
    #                   country='fr',
    #                   country_alttext='The flag of France.',
    #                   monument='Eiffel Tower',
    #                   monument_alttext='A picture of the Eiffel Tower during the day, functioning as a placeholder.',
    #                   description='This is where an actual description of the monument would go, going into its history and such. However,  this isn\'t a real website,  so enjoy the filler text below.')
    # db.session.add(minument4)

    # # 05 - UNITED TOWER
    # minument5 = Items(id=5,
    #                   city='MANAMA',
    #                   country='bh',
    #                   country_alttext='The flag of Bahrain.',
    #                   monument='United Tower',
    #                   monument_alttext='A picture of the United Tower during dusk/dawn, functioning as a placeholder.',
    #                   description='This is where an actual description of the monument would go, going into its history and such. However,  this isn\'t a real website,  so enjoy the filler text below.')
    # db.session.add(minument5)

    # # 06 - GATEWAY ARCH
    # minument6 = Items(id=6,
    #                   city='ST. LOUIS',
    #                   country='us',
    #                   country_alttext='The flag of the United States.',
    #                   monument='Gateway Arch',
    #                   monument_alttext='A picture of the Gateway Arch during dusk/dawn, functioning as a placeholder.',
    #                   description='This is where an actual description of the monument would go, going into its history and such. However,  this isn\'t a real website,  so enjoy the filler text below.')
    # db.session.add(minument6)


    # # TAGS ==================================================================================================

    # # 01 - AFRICA
    # tag1 = Tags(id=1,
    #             name='AFRICA')
    # db.session.add(tag1)

    # # 02 - ASIA
    # tag2 = Tags(id=2,
    #             name='ASIA')
    # db.session.add(tag2)

    # # 03 - EUROPE
    # tag3 = Tags(id=3,
    #             name='EUROPE')
    # db.session.add(tag3)

    # # 04 - NORTH AMERICA
    # tag4 = Tags(id=4,
    #             name='NORTH AMERICA')
    # db.session.add(tag4)

    # # 05 - SOUTH AMERICA
    # tag5 = Tags(id=5,
    #             name='AFRICA')
    # db.session.add(tag5)

    # # 06 - OCEANIA
    # tag6 = Tags(id=6,
    #             name='OCEANIA')
    # db.session.add(tag6)

    # # 07 - OLDEN
    # tag7 = Tags(id=7,
    #             name='AFRICA')
    # db.session.add(tag7)

    # # 08 - MODERN
    # tag8 = Tags(id=8,
    #             name='MODERN')
    # db.session.add(tag8)


    # # ITEMTAGS ==================================================================================================

    # # 01 - RIFFA CLOCK TOWER
    # itemTagList = [[1, 2]]
    # itemtag1 = ItemTags(itemid=1,
    #                     tagid=2)
    # db.session.add(itemtag1)
    # itemtag2 = ItemTags(itemid=1,
    #                     tagid=8)
    # db.session.add(itemtag2)

    # db.session.add(minument1)