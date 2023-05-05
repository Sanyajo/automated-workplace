host = "127.0.0.1"
user = "postgres"
password = "Sasaha228"
db_name = "kurs"

list_typegsm = ['Код ГСМ', 'Название ГСМ', 'Единица измерения']
list_vendorgsm=['Код поставщика', 'Название производителя', 'Адрес производителя', 'Код ГСМ']
list_companydrivers=['Табельный номер\n водителя', 'ФИО водителя', 'Государственный но\nмер прикрепленного авто', 'Дата приема\n на работу', '\tДата выдачи\n водительсокого удостоверения', '\tДата действия\n водительсокого удостоверения', 'Номер водительского\n удостоверения', 'Категория водительского\n удостоверения']
list_comptechnmeans=['НомГосРегистр', 'Марка авто', 'Номер кузова', 'ЕдИмз', 'Грузоподъёмность', 'Год выпусмка', 'Первичная стоимость', 'Код %', 'Остаточная стоимость']
list_deliverycontract=['Номер договора','Дата заключения\n договора','Код ГСМ','Код поставщика','Единица\n измерения','Цена','Количество','Стоимость','Ставка НДС','Сумма НДС','Сумма с НДС']
list_naryad=['Номер наряда','Дата составления','Табельный номер\nводителя','ФИО водителя','Государственный номер\nавто','Номер водительского\n удостоверения','Производимая работа']
list_pl=['Номер путевого\nлиста','Дата составления ПЛ','Табельный номер\nводителя','Номер водительского\nудостоверения','Государственный номер\nавто','Единица измерения','Цена','Количество','Стоимость','Ставка НДС','Сумма НДС','Сумма с НДС']
list_prihod=['Номер документа','Дата составленеия','Номер ТТН','Дата ТТН','Код ГСМ','Код поставщика','Единица измерения','Количество','Цена','Ставка НДС']
list_rashod=['Номер документа','Номер ПЛ','Дата ПЛ','Код ГСМ','Единица измерения','Количество','Цена','Ставка НДС']
list_ksu=['Номер документа','Код ГСМ','Код поставщика','Номер склада','Номер цистерны','Дата составления\nКСУ','Единица измерения','Стоимость единицы','Остаток на начало\nпериода','Количество прихода','Количество расхода','Остаток на конец\nпериода']
list_ttn=['Номер документа','Дата ТТН','Код ГСМ','Код поставщика','Единица измерения','Цена','Количество','Стоимость','Ставка НДС','Сумма НДС','Сумма с НДС']


slist_typegsm = ['КодГСМ','НазвГСМ','ЕдИзм']
slist_vendorgsm = ['КодПост','НазвПроизв','АдрПроизв','КодГСМ']
slist_companydrivers = ['ТабНомВод','ФИОвод','ГосНомПрикрАвто','ДатПриемНаРаб','ДатВыдВодУдост','ДатДействВодУдост','НомВодУдост','КатВодУдост']
slist_comptechnmeans = ['НомГосРег', 'МаркАвт', 'НомКуз', 'ЕдИзм', 'Грузоп', 'ГодВып', 'ПервСтоим', 'Код %', 'ОстаСтоим']
slist_deliverycontract = ['НомДог','ДатЗаклДог','КодГСМ','КодПост','ЕдИзм','Цена','Кол','Стоим','СтавкНДС','СуммНДС','Сумм c НДС']
slist_naryad = ['НомНар','ДатСост','ТабНомВод','ФИОвод','ГосНомАвто','НомВодУдост','ПроизвРаб']
slist_pl = ['НомПутЛист','ДатаСостПЛ','ТабНомВод','НомВодУдост','ГосНомАвто','ЕдИзм','Цена','Кол','Стоим','СтавкНДС','СуммНДС','Сумм с НДС']
slist_prihod = ['НомДок','ДатСост','НомТТН','ДатТТН','КодГСМ','КодПост','ЕдИзм','Кол','Цена','СтавкНДС']
slist_rashod = ['НомДок','НомПЛ','ДатПЛ','КодГСМ','ЕдИзм','Кол','Цена','СтавкНДС']
slist_ksu = ['НомСкл','НомЦист','НомДок','КодГСМ','КодПост','ДатСостКСУ','ЕдИзм','CтоимЕд','ОстНаНачПер','КолПрих','КолРасх','ОстаНаКонПер']
slist_ttn = ['НомДок','ДатТТН','КодГСМ','КодПост','ЕдИзм','Цена','Кол','Стоим','СтавкНДС','СуммНДС','Сумм с НДС']

searhListINT = ["Цена", "Количество", "Стоим",'Кол',
                "СтавкНДС", "Сумма НДС", "Сумма с НДС",'СуммНДС',
                "CтоимЕд", "ОстНаНачПер", "КолПрих", "КолРасх",
                "ОстаНаКонПер", "Грузоп", "ГодВып", "ПервСтоим", "Код %", "ОстаСтоим"]
searhSQLListINT = {
    ('ttn','Цена'):'price',
    ('ttn','Кол'):'amount',
    ('ttn','Стоим'):'stoim',
    ('ttn','СтавкНДС'):'rate_nds',
    ('ttn','СуммНДС'):'price_nds',
    ('ttn','Сумм с НДС'):'price_of_nds',
    ('rashfile','Кол'):'amount',
    ('rashfile','Цена'):'price',
    ('rashfile','СтавкНДС'):'rate_nds',
    ('prihfile', 'Кол'):'amount',
    ('prihfile', 'Цена'):'price',
    ('prihfile', 'СтавкНДС'):'rate_nds',
    ('ksu','СтоимЕд'):'ed_price',
    ('ksu','ОстНаНачПер'):'start_bal',
    ('ksu','КолПрих'):'amount_prih_gsm',
    ('ksu','КолРасх'):'amount_rash_gsm',
    ('ksu','ОстаНаКонПер'):'end_bal',
    ('deliverycontract','Цена'):'price',
    ('deliverycontract','Кол'):'amount',
    ('deliverycontract','Стоим'):'stoim',
    ('deliverycontract','СтавкНДС'):'rate_nds',
    ('deliverycontract','СуммНДС'):'price_nds',
    ('deliverycontract','Сумм с НДС'):'price_of_nds',
    ('comptechnmeans','Грузоп'):'load_capacity',
    ('comptechnmeans','ГодВып'):'year_of_product',
    ('comptechnmeans','ПервСтоим'):'first_cost',
    ('comptechnmeans','Код %'):'kod_porc',
    ('comptechnmeans','ОстаСтоим'):'last_cost',
    ('pl','Цена'):'price',
    ('pl','Кол'):'amount',
    ('pl','Стоим'):'stoim',
    ('pl','СтавкНДС'):'rate_nds',
    ('pl','СуммНДС'):'price_nds',
    ('pl','Сумм с НДС'):'price_of_nds',
}

searhList = ['КодГСМ','НазвГСМ','ЕдИзм',
             'КодПост','НазвПроизв','АдрПроизв',
             'ТабНомВод','ФИОвод','ГосНомПрикрАвто',
             'ДатПриемНаРаб','ДатВыдВодУдост','ДатДействВодУдост',
             'НомВодУдост','КатВодУдост','НомГосРег','МаркАвт',
             'НомКуз','НомДог','ДатЗаклДог','НомНар','НомПутЛист',
             'ДатаСостПЛ','НомДок','ДатСост','НомТТН','ДатТТН','НомПЛ',
             'ДатПЛ','НомСкл','НомЦист','ДатСостКСУ','ПроизвРаб']
searhSQLList = {
    ('vendorgsm','КодПост'):'code_post',
    ('vendorgsm','НазвПроизв'):'name_proizv',
    ('vendorgsm','АдрПроизв'):'addres_proizv',
    ('vendorgsm','КодГСМ'):'code_gsm',
    ('typegsm','КодГСМ'):'code_gsm',
    ('typegsm','НазвГСМ'):'name_gsm',
    ('typegsm','ЕдИзм'):'unit',
    ('companydrivers','ТабНомВод'):'tab_number',
    ('companydrivers','ФИОвод'):'drivers_name',
    ('companydrivers','ГосНомПрикрАвто'):'national_avto_num',
    ('companydrivers','ДатПриемНаРаб'):'date_of_hire',
    ('companydrivers','ДатВыдВодУдост'):'date_driverlicens',
    ('companydrivers','ДатДействВодУдост'):'validity_day_drlic',
    ('companydrivers','НомВодУдост'):'num_drivlicens',
    ('companydrivers','КатВодУдост'):'category_drivlicens',
    ('comptechnmeans','НомГосРег'):'national_avto_num',
    ('comptechnmeans','МаркАвт'):'auto_mark',
    ('comptechnmeans','НомКуз'):'body_number',
    ('comptechnmeans','ЕдИзм'):'untill',
    ('deliverycontract','НомДог'):'contract_number',
    ('deliverycontract','ДатЗаклДог'):'date_contract',
    ('deliverycontract','КодГСМ'):'code_gsm',
    ('deliverycontract','КодПост'):'code_post',
    ('naryad','НомНар'):'nar_number',
    ('naryad','ТабНомВод'):'tab_number',
    ('naryad','ФИОвод'):'drivers_name',
    ('naryad','ГосНомАвто'):'national_avto_num',
    ('naryad','НомВодУдост'):'num_drivlicens',
    ('naryad','ПроизвРаб'):'rabot',
    ('naryad','ДатСост'):'date_nar',
    ('pl','НомПутЛист'):'pl_number',
    ('pl','ДатаСостПЛ'):'date_pl',
    ('pl','ТабНомВод'):'tab_number',
    ('pl','НомВодУдост'):'num_drivlicens',
    ('pl','ГосНомАвто'):'national_avto_num',
    ('pl','ЕдИзм'):'unit',
    ('prihfile','НомДок'):'doc_number_prih',
    ('prihfile','ДатСост'):'date_sost',
    ('prihfile','НомТТН'):'ttn_number',
    ('prihfile','ДатТТН'):'date_zakl_ttn',
    ('prihfile','КодГСМ'):'code_gsm',
    ('prihfile','КодПост'):'code_post',
    ('prihfile','ЕдИзм'):'untill',
    ('rashfile','НомДок'):'prih_number',
    ('rashfile','НомПЛ'):'pl_number',
    ('rashfile','ДатПЛ'):'date_pl',
    ('rashfile','КодГСМ'):'code_gsm',
    ('rashfile','ЕдИзм'):'unit',
    ('ksu','НомДок'):'ksu_doc',
    ('ksu','КодГСМ'):'code_gsm',
    ('ksu','КодПост'):'code_post',
    ('ksu','НомСкл'):'sklad_number',
    ('ksu','НомЦист'):'tanker_number',
    ('ksu','ДатСостКСУ'):'date_ksu',
    ('ksu','ЕдИзм'):'unit',
    ('ttn','НомДок'):'ttn_number',
    ('ttn','ДатТТН'):'date_zakl_ttn',
    ('ttn','КодГСМ'):'code_gsm',
    ('ttn','КодПост'):'code_post',
    ('ttn','ЕдИзм'):'untill'
}

searhComboboxList = {
    'typegsm':slist_typegsm,
    'vendorgsm':slist_vendorgsm,
    'companydrivers':slist_companydrivers,
    'deliverycontract':slist_deliverycontract,
    'naryad':slist_naryad,
    'pl':slist_pl,
    'prihod':slist_prihod,
    'rashod':slist_rashod,
    'ksu':slist_ksu,
    'ttn':slist_ttn
}

searhComboboxList1 = {
    'typegsm':list_typegsm,
    'vendorgsm':list_vendorgsm,
    'companydrivers':list_companydrivers,
    'deliverycontract':list_deliverycontract,
    'naryad':list_naryad,
    'pl':list_pl,
    'prihod':list_prihod,
    'rashod':list_rashod,
    'ksu':list_ksu,
    'ttn':list_ttn
}