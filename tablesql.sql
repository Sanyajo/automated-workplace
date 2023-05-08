-- CREATE TABLE TypeGSM(
-- 	code_gsm CHARACTER VARYING(12) PRIMARY KEY NOT NULL,
-- 	name_gsm CHARACTER VARYING(30) NOT NULL,
-- 	unit CHARACTER VARYING(3) NOT NULL
-- );

-- CREATE TABLE VendorGSM(
-- 	code_post CHARACTER VARYING(7) NOT NULL,
-- 	name_proizv CHARACTER VARYING(30) NOT NULL,
-- 	addres_proizv TEXT NOT NULL,
-- 	code_gsm CHARACTER VARYING(12) REFERENCES typegsm(code_gsm) ON UPDATE CASCADE ON DELETE CASCADE NOT NULL,
-- 	PRIMARY KEY(code_post)
-- );

-- CREATE TABLE CompanyDrivers(
-- 	tab_number CHARACTER VARYING(6) NOT NULL,
-- 	drivers_name CHARACTER VARYING(50) NOT NULL,
-- 	national_avto_num CHARACTER VARYING(10) NOT NULL,
-- 	date_of_hire CHARACTER VARYING(10) NOT NULL,
-- 	date_driverlicens CHARACTER VARYING(10) NOT NULL,
-- 	validity_day_drlic CHARACTER VARYING(10) NOT NULL,
-- 	num_drivlicens CHARACTER VARYING(10) NOT NULL,
-- 	category_drivlicens CHARACTER VARYING(3) NOT NULL,
-- 	PRIMARY KEY(tab_number, num_drivlicens)
-- );

-- CREATE TABLE TTN(
-- 	ttn_number CHARACTER VARYING(7) NOT NULL,
-- 	date_zakl_ttn CHARACTER VARYING(11) NOT NULL,
-- 	code_gsm CHARACTER VARYING(12) REFERENCES TypeGSM(code_gsm) ON UPDATE CASCADE ON DELETE CASCADE NOT NULL,
-- 	code_post CHARACTER VARYING(8) REFERENCES VendorGSM(code_post) ON UPDATE CASCADE ON DELETE CASCADE NOT NULL,
-- 	untill CHARACTER VARYING(3) NOT NULL,
-- 	amount INTEGER NOT NULL,
	
-- 	PRIMARY KEY(ttn_number,code_gsm,code_post)
-- );

-- CREATE UNIQUE INDEX ttn_unique_key ON TTN(ttn_number, date_zakl_ttn);

-- CREATE TABLE DeliveryContract(
-- 	contract_number CHARACTER VARYING(10) NOT NULL,
-- 	date_contract CHARACTER VARYING(11) NOT NULL,
-- 	code_gsm CHARACTER VARYING(12) NOT NULL,
-- 	code_post CHARACTER VARYING(8) NOT NULL,
-- 	untill CHARACTER VARYING(3) NOT NULL,
-- 	price INTEGER NOT NULL,
-- 	amount INTEGER NOT NULL,
-- 	stoim INTEGER NOT NULL,
-- 	rate_NDS INTEGER NOT NULL,
-- 	price_NDS INTEGER NOT NULL,
-- 	price_of_NDS INTEGER NOT NULL,
-- 	PRIMARY KEY(contract_number, date_contract),
-- 	FOREIGN KEY (code_gsm) REFERENCES TypeGSM(code_gsm) ON UPDATE CASCADE ON DELETE CASCADE,
-- 	FOREIGN KEY (code_post) REFERENCES VendorGSM(code_post) ON UPDATE CASCADE ON DELETE CASCADE
-- );

-- ALTER TABLE DeliveryContract ADD CONSTRAINT unique_code_gsm UNIQUE (code_gsm);
-- ALTER TABLE DeliveryContract ADD CONSTRAINT unique_code_post UNIQUE (code_post);
-- ALTER TABLE ttn ADD CONSTRAINT unique_ttn UNIQUE (ttn_number, code_gsm, code_post);
-- -- CREATE UNIQUE INDEX unk ON TTN(code_gsm, code_post);

-- CREATE TABLE PrihFile(
--     doc_number_prih BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
--     date_sost CHARACTER VARYING(11) NOT NULL,
--     ttn_number CHARACTER VARYING(7) NOT NULL,
--     date_zakl_ttn CHARACTER VARYING(11) NOT NULL,
--     code_gsm CHARACTER VARYING(12) NOT NULL,
--     code_post CHARACTER VARYING(8) NOT NULL,
--     untill CHARACTER VARYING(3) NOT NULL,
--     amount DOUBLE PRECISION NOT NULL,
--     FOREIGN KEY (ttn_number, code_gsm, code_post) REFERENCES ttn(ttn_number, code_gsm, code_post) ON UPDATE CASCADE ON DELETE CASCADE
-- );
-- CREATE UNIQUE INDEX TTN_unique_idx ON TTN (ttn_number, date_zakl_ttn, code_gsm, code_post);


-- CREATE TABLE CompanyDrivers(
--     tab_number CHARACTER VARYING(6) NOT NULL,
--     drivers_name CHARACTER VARYING(50) NOT NULL,
--     national_avto_num CHARACTER VARYING(10) NOT NULL,
--     date_of_hire CHARACTER VARYING(10) NOT NULL,
--     date_driverlicens CHARACTER VARYING(10) NOT NULL,
--     validity_day_drlic CHARACTER VARYING(10) NOT NULL,
--     num_drivlicens CHARACTER VARYING(10) NOT NULL,
--     category_drivlicens CHARACTER VARYING(3) NOT NULL,
--     PRIMARY KEY(tab_number, num_drivlicens)
-- );

-- CREATE TABLE CompTechnMeans(
--     national_avto_num CHARACTER VARYING(10) NOT NULL,
--     auto_mark CHARACTER VARYING(20) NOT NULL,
--     body_number CHARACTER VARYING(20) NOT NULL,
--     untill CHARACTER VARYING(3) NOT NULL,
--     load_capacity INTEGER NOT NULL,
--     year_of_product INTEGER NOT NULL,
--     first_cost INTEGER NOT NULL,
--     kod_porc CHARACTER VARYING(20) NOT NULL,
--     last_cost INTEGER NOT NULL,
--     PRIMARY KEY(national_avto_num, auto_mark, body_number)
-- );

-- ALTER TABLE CompTechnMeans ADD CONSTRAINT unique_comptechnmeans UNIQUE (national_avto_num);



-- CREATE OR REPLACE FUNCTION update_probeg() RETURNS trigger AS $$
-- DECLARE
--     total_probeg DOUBLE PRECISION;
-- BEGIN
--     IF TG_OP = 'DELETE' THEN
--         SELECT COUNT(*) INTO total_probeg FROM pl WHERE national_avto_num = OLD.national_avto_num;
--         IF total_probeg = 0 THEN
--             UPDATE CompTechnMeans
--             SET last_cost = 0
--             WHERE national_avto_num = OLD.national_avto_num;
--         ELSE
--             UPDATE CompTechnMeans
--             SET last_cost = (first_cost - (total_probeg * 0.22 + 0.62 * (2023 - year_of_product)))
        
--             WHERE national_avto_num = OLD.national_avto_num;
--         END IF;
--     ELSE
--         SELECT SUM(pl.probeg) INTO total_probeg FROM pl WHERE national_avto_num = NEW.national_avto_num;
--         UPDATE CompTechnMeans
--         SET last_cost = (first_cost - (total_probeg * 0.22 + 0.62 * (2023 - year_of_product)))

--         WHERE national_avto_num = NEW.national_avto_num;
--     END IF;
    
--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;






-- CREATE TRIGGER trg_update_probe
-- AFTER INSERT ON pl
-- FOR EACH ROW
-- EXECUTE FUNCTION update_probeg();

-- CREATE TRIGGER trg_DELETE_probeg
-- AFTER DELETE ON pl
-- FOR EACH ROW
-- EXECUTE FUNCTION update_probeg();

-- CREATE TRIGGER trg_up_probeg
-- AFTER UPDATE ON pl
-- FOR EACH ROW
-- EXECUTE FUNCTION update_probeg();






-- CREATE TABLE naryad (
--     nar_number CHARACTER VARYING(10) NOT NULL,
-- 	date_nar CHARACTER VARYING(11) NOT NULL,
--     tab_number CHARACTER VARYING(6) NOT NULL,
--     drivers_name TEXT NOT NULL,
--     national_avto_num CHARACTER VARYING(10) NOT NULL,
--     num_drivlicens CHARACTER VARYING(10) NOT NULL,
-- 	rabot CHARACTER VARYING(10) NOT NULL,
-- 	PRIMARY KEY (nar_number, rabot),
--     FOREIGN KEY (national_avto_num) REFERENCES CompTechnMeans (national_avto_num) ON UPDATE CASCADE ON DELETE CASCADE,
--     FOREIGN KEY (tab_number, num_drivlicens) REFERENCES CompanyDrivers (tab_number, num_drivlicens) ON UPDATE CASCADE ON DELETE CASCADE
-- );

-- ALTER TABLE naryad ADD CONSTRAINT unique_tab1 UNIQUE (tab_number, national_avto_num,rabot);
-- -- ALTER TABLE naryad ADD CONSTRAINT unique_tab2 UNIQUE (rabot);


-- CREATE TABLE PL (
--     pl_number CHARACTER VARYING(10) NOT NULL PRIMARY KEY,
--     date_pl CHARACTER VARYING(11) NOT NULL,
-- 	code_gsm CHARACTER VARYING(12) NOT NULL,
-- 	tab_number CHARACTER VARYING(6) NOT NULL,
--     num_drivlicens CHARACTER VARYING(10) NOT NULL,
--     national_avto_num CHARACTER VARYING(10) NOT NULL,
-- 	probeg DOUBLE PRECISION NOT NULL,
-- 	unit CHARACTER VARYING(3) NOT NULL,
-- 	ostatok DOUBLE PRECISION NOT NULL,
-- 	amount DOUBLE PRECISION NOT NULL,
-- 	potr DOUBLE PRECISION NOT NULL,
-- -- 	FOREIGN KEY (pl_number) REFERENCES naryad (rabot) ON UPDATE CASCADE ON DELETE CASCADE,
--     FOREIGN KEY (num_drivlicens) REFERENCES CompanyDrivers (num_drivlicens) ON UPDATE CASCADE ON DELETE CASCADE,
--     FOREIGN KEY (tab_number, national_avto_num,pl_number) REFERENCES naryad (tab_number, national_avto_num,rabot) ON UPDATE CASCADE ON DELETE CASCADE,
--     FOREIGN KEY (national_avto_num) REFERENCES CompTechnMeans (national_avto_num) ON UPDATE CASCADE ON DELETE CASCADE
-- );

-- -- -- -- Создание уникального ключа для таблицы CompTechnMeans
-- -- -- ALTER TABLE CompTechnMeans ADD CONSTRAINT unique_national_avto_num UNIQUE (national_avto_num);
--  ALTER TABLE PL ADD CONSTRAINT unique_pl_number_date UNIQUE (pl_number,code_gsm);



-- CREATE TABLE rashfile(
--     prih_number BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
--     date_sost CHARACTER VARYING(11) NOT NULL,
--     pl_number CHARACTER VARYING(10) NOT NULL,
--     date_pl CHARACTER VARYING(10) NOT NULL,
--     code_gsm CHARACTER VARYING(12) NOT NULL,
--     unit CHARACTER VARYING(3) NOT NULL,
--     amount INTEGER NOT NULL
-- );
-- ALTER TABLE rashfile ADD CONSTRAINT unique_rashfile UNIQUE (pl_number,code_gsm);

-- CREATE OR REPLACE FUNCTION update_rashfile() RETURNS TRIGGER AS $$
-- BEGIN
--     IF TG_OP = 'DELETE' THEN
--         -- Удаление данных из таблицы rashfile при удалении данных из PL
--         DELETE FROM rashfile WHERE pl_number = OLD.pl_number AND date_pl = OLD.date_pl AND code_gsm = OLD.code_gsm;
--     ELSIF TG_OP = 'UPDATE' THEN
--         -- Изменение данных в таблице rashfile при изменении данных в PL
--         UPDATE rashfile SET date_sost = NEW.date_pl, pl_number = NEW.pl_number, date_pl = NEW.date_pl, code_gsm = NEW.code_gsm, unit = NEW.unit, amount = NEW.amount
--         WHERE pl_number = NEW.pl_number AND date_pl = NEW.date_pl AND code_gsm = NEW.code_gsm;
--     ELSIF TG_OP = 'INSERT' THEN
--         -- Добавление данных в таблицу rashfile при добавлении данных в PL
--         INSERT INTO rashfile (date_sost, pl_number, date_pl, code_gsm, unit, amount)
--         VALUES (NEW.date_pl, NEW.pl_number, NEW.date_pl, NEW.code_gsm, NEW.unit, NEW.amount);
--     END IF;
    
--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE TRIGGER trg_update_rashfile
-- AFTER DELETE OR UPDATE OR INSERT ON PL
-- FOR EACH ROW
-- EXECUTE FUNCTION update_rashfile();


-- CREATE TABLE KSU(
-- 	ksu_doc CHARACTER VARYING(10) NOT NULL,
-- 	date_ksu CHARACTER VARYING(11) NOT NULL,
-- 	sklad_number CHARACTER VARYING(10) NOT NULL,
-- 	tanker_number CHARACTER VARYING(8) NOT NULL,
-- 	code_gsm CHARACTER VARYING(12) NOT NULL,
-- 	code_post CHARACTER VARYING(8) NOT NULL,
-- 	unit CHARACTER VARYING(3) NOT NULL,
-- 	ed_price DOUBLE PRECISION NOT NULL,
-- 	start_bal DOUBLE PRECISION NOT NULL,
-- 	amount_prih_gsm DOUBLE PRECISION NOT NULL,
-- 	amount_rash_gsm DOUBLE PRECISION NOT NULL,
-- 	end_bal DOUBLE PRECISION NOT NULL,
-- 	PRIMARY KEY(ksu_doc, sklad_number, tanker_number, date_ksu),
-- 	FOREIGN KEY(code_gsm) REFERENCES typegsm(code_gsm) ON UPDATE CASCADE ON DELETE CASCADE,
-- 	FOREIGN KEY(code_post) REFERENCES vendorgsm(code_post) ON UPDATE CASCADE ON DELETE CASCADE
-- );
-- ALTER TABLE KSU ADD CONSTRAINT unique_KSU UNIQUE (ksu_doc,code_gsm,code_post);



-- CREATE OR REPLACE FUNCTION sync_prihfile()
-- RETURNS TRIGGER AS $$
-- BEGIN
--     IF TG_OP = 'DELETE' THEN
--         -- Удаление данных из таблицы PrihFile при удалении данных из TTN
--         DELETE FROM PrihFile WHERE ttn_number = OLD.ttn_number AND date_zakl_ttn = OLD.date_zakl_ttn AND code_gsm = OLD.code_gsm AND code_post = OLD.code_post;
--     ELSIF TG_OP = 'UPDATE' THEN
--         -- Изменение данных в таблице PrihFile при изменении данных в TTN
--         UPDATE PrihFile SET date_sost = NEW.date_zakl_ttn, untill = NEW.untill, amount = NEW.amount
--         WHERE ttn_number = NEW.ttn_number AND date_zakl_ttn = NEW.date_zakl_ttn AND code_gsm = NEW.code_gsm AND code_post = NEW.code_post;
--     ELSIF TG_OP = 'INSERT' THEN
--         -- Добавление данных в таблицу PrihFile при добавлении данных в TTN
--         INSERT INTO PrihFile (date_sost, ttn_number, date_zakl_ttn, code_gsm, code_post, untill, amount)
--         VALUES (NEW.date_zakl_ttn, NEW.ttn_number, NEW.date_zakl_ttn, NEW.code_gsm, NEW.code_post, NEW.untill, NEW.amount);
--     END IF;

--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE TRIGGER trg_sync_prihfile
-- AFTER DELETE OR UPDATE OR INSERT ON TTN
-- FOR EACH ROW
-- EXECUTE FUNCTION sync_prihfile();




-- CREATE OR REPLACE FUNCTION update_ksu_amount()
-- RETURNS TRIGGER AS $$
-- DECLARE
--     total_prih NUMERIC;
--     total_rash NUMERIC;
-- BEGIN
--     -- Рассчитываем сумму приходов для данного code_gsm в таблице ttn
--     SELECT COALESCE(SUM(amount), 0) INTO total_prih
--     FROM ttn
--     WHERE code_gsm = NEW.code_gsm;

--     -- Рассчитываем сумму расходов для данного code_gsm в таблице pl
--     SELECT COALESCE(SUM(amount), 0) INTO total_rash
--     FROM pl
--     WHERE code_gsm = NEW.code_gsm;

--     -- Если записи в ttn или pl не найдены, устанавливаем значения 0
--     IF total_prih IS NULL THEN
--         total_prih := 0;
--     END IF;

--     IF total_rash IS NULL THEN
--         total_rash := 0;
--     END IF;

--     -- Обновляем значения amount_prih_gsm, amount_rash_gsm и end_bal в таблице ksu
--     UPDATE ksu
--     SET amount_prih_gsm = total_prih,
--         amount_rash_gsm = total_rash,
--         end_bal = start_bal + total_prih - total_rash
--     WHERE code_gsm = NEW.code_gsm;

--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE TRIGGER trg_update_ksu_amount
-- AFTER INSERT OR UPDATE OR DELETE ON ttn
-- FOR EACH ROW
-- EXECUTE FUNCTION update_ksu_amount();

-- CREATE TRIGGER trg_update_ksu_amount_pl
-- AFTER INSERT OR UPDATE OR DELETE ON pl
-- FOR EACH ROW
-- EXECUTE FUNCTION update_ksu_amount();