host = ""
user = ""
password = ""
db_name = ""

list_typegsm = ['Код ГСМ', 'Название ГСМ', 'Единица измерения']
list_vendorgsm=['Код поставщика', 'Название производителя', 'Адрес производителя', 'Код ГСМ']
list_companydrivers=['Табельный номер\n водителя', 'ФИО водителя', 'Государственный но\nмер прикрепленного авто', 'Дата приема\n на работу', '\tДата выдачи\n водительсокого удостоверения', '\tДата действия\n водительсокого удостоверения', 'Номер водительского\n удостоверения', 'Категория водительского\n удостоверения']
list_comptechnmeans=['НомГосРегистр', 'Марка авто', 'Номер кузова', 'ЕдИмз', 'Грузоподъёмность', 'Год выпусмка', 'Первичная стоимость', 'Код %', 'Остаточная стоимость']
list_deliverycontract=['Номер договора','Дата заключения\n договора','Код ГСМ','Код поставщика','Единица\n измерения','Цена','Количество','Стоимость','Ставка НДС','Сумма НДС','Сумма с НДС']
list_naryad=['Номер наряда','Дата составления','Табельный номер\nводителя','ФИО водителя','Государственный номер\nавто','Номер водительского\n удостоверения','Производимая работа']
list_pl=['Номер путевого листа','Дата составления ПЛ','Код ГСМ','Табельный номер водителя','Номер водительского\nудостоверения','Государственный номер авто','Пробег, км','Единица измерения','Остаток ГСМ','Объем полученных ГСМ','Объем потраченных ГСМ']
list_prihod=['Номер документа','Дата составленеия','Номер ТТН','Дата ТТН','Код ГСМ','Код поставщика','Единица измерения','Количество']
list_rashod=['Номер документа','Дата составления','Номер ПЛ','Дата ПЛ','Код ГСМ','Единица измерения','Количество']
list_ksu=['Номер документа','Дата составления\nКСУ','Номер склада','Номер цистерны','Код ГСМ','Код поставщика','Единица измерения','Стоимость единицы','Остаток на начало\nпериода','Количество прихода','Количество расхода','Остаток на конец\nпериода']
list_ttn=['Номер документа','Дата ТТН','Код ГСМ','Код поставщика','Единица измерения','Количество']


slist_typegsm = ['КодГСМ','НазвГСМ','ЕдИзм']
slist_vendorgsm = ['КодПост','НазвПроизв','АдрПроизв','КодГСМ']
slist_companydrivers = ['ТабНомВод','ФИОвод','ГосНомПрикрАвто','ДатПриемНаРаб','ДатВыдВодУдост','ДатДействВодУдост','НомВодУдост','КатВодУдост']
slist_comptechnmeans = ['НомГосРег', 'МаркАвт', 'НомКуз', 'ЕдИзм', 'Грузоп', 'ГодВып', 'ПервСтоим', 'Код %', 'ОстаСтоим']
slist_deliverycontract = ['НомДог','ДатЗаклДог','КодГСМ','КодПост','ЕдИзм','Цена','Кол','Стоим','СтавкНДС','СуммНДС','Сумм c НДС']
slist_naryad = ['НомНар','ДатСост','ТабНомВод','ФИОвод','ГосНомАвто','НомВодУдост','ПроизвРаб']
slist_pl = ['НомПутЛист','ДатаСостПЛ','КодГСМ','ТабНомВод','НомВодУдост','ГосНомАвто','Пробег, км','ЕдИзм','ОстГСМ','ОбПолГСМ','ОбПотрГСМ']
slist_prihod = ['НомДок','ДатСост','НомТТН','ДатТТН','КодГСМ','КодПост','ЕдИзм','Кол']
slist_rashod = ['НомДок','ДатCост','НомПЛ','ДатПЛ','КодГСМ','ЕдИзм','Кол']
slist_ksu = ['НомДок','ДатСостКСУ','НомСкл','НомЦист','КодГСМ','КодПост','ЕдИзм','CтоимЕд','ОстНаНачПер','КолПрих','КолРасх','ОстаНаКонПер']
slist_ttn = ['НомДок','ДатТТН','КодГСМ','КодПост','ЕдИзм','Кол']

searhListINT = ["Цена", "Кол", "Стоим",'ОбПолГСМ',
                "СтавкНДС", "Сумма НДС", "Сумма с НДС",'СуммНДС',
                "CтоимЕд", "ОстНаНачПер", "КолПрих", "КолРасх",
                "ОстаНаКонПер", "Грузоп", "ГодВып", "ПервСтоим", "Код %", "ОстаСтоим","Пробег, км","ОстГСМ","ОбПотрГСМ"]
searhSQLListINT = {
    ('ttn','Кол'):'amount',
    ('rashfile','Кол'):'amount',
    ('prihfile', 'Кол'):'amount',
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
    ('pl','ОбПолГСМ'):'amount',
    ('pl','Пробег, км'):'probeg',
    ('pl','ОстГСМ'):'ostatok',
    ('pl','ОбПотрГСМ'):'potr'
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
    ('pl','КодГСМ'):'сode_gsm',
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
    ('rashfile','ДатСост'):'date_sost',
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
    'prihfile':slist_prihod,
    'rashfile':slist_rashod,
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
    'prihfile':list_prihod,
    'rashfile':list_rashod,
    'ksu':list_ksu,
    'ttn':list_ttn
}

list_otch1 = [[],[]]