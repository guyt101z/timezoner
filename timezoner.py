import time

def DST_day(yr,begin):
    if begin == 0:
        DST_date = [10,9,8,13]
        return DST_date[yr-2013]
    elif begin == 1:
        DST_date = [3,2,1,6]
        return DST_date[yr-2013]

def check_DST(local_tim):
    check_val =((local_tim.tm_mon  > 3 and local_tim.tm_mon  < 11 ) or
            (local_tim.tm_mon  == 3 and local_tim.tm_mday > DST_day(local_tim.tm_year,0)) or
            (local_tim.tm_mon  == 11 and DST_day(local_tim.tm_year,1) < local_tim.tm_mday) or
            (local_tim.tm_mon  == 3 and local_tim.tm_mday == DST_day(local_tim.tm_year,0 ) and local_tim.tm_hour >= 2) or
            (local_tim.tm_mon  == 11 and DST_day(local_tim.tm_year,1) == local_tim.tm_mday  and local_tim.tm_hour < 1))
    return check_val

def timezone_est(tim, loc): #tim is assumed to be in miliseconds, and loc contains a state designation
    tim = tim/1000.0 #convert time to seconds
    lay_tim  = time.gmtime(tim)
    Somoa_tz = -11; HST_tz = -10; AKST_tz = -9; PST_tz = -8; MST_tz = -7; CST_tz = -6
    EST_tz = -5; AST_tz = -4; Palau_tz = 9; ChSt_tz = 10; MHT_tz = 12

    ###CENTRAL###
    if (loc.find(', AL ') >= 0 or loc.find(', AR ') >= 0 or loc.find(', IL ') >= 0 or loc.find(', IA ') >= 0 or
        loc.find(', LA ') >= 0 or loc.find(', MN ') >= 0 or loc.find(', MS ') >= 0 or
        loc.find(', OK ') >= 0 or loc.find(', WI ') >= 0 or loc.find(', MO ') >= 0):
        gmt_offset = CST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)
        #modify for daylight savings time:
        if check_DST(local_tim):
            local_tim  = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###ALASKA###
    elif loc.find(', AK ') >= 0:
        for z in ['99546','99547','99553','99571','99583','99591','99612','99638','99660','99661','99685','99692']:
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = HST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = AKST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim  = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###ARIZONA###
    elif loc.find(', AZ ') >= 0:
        #Note that we have not accounted for the Navajo Nation
        gmt_offset = MST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###PACIFIC###
    elif loc.find(', CA ') >= 0 or loc.find(', WA ') >= 0 or loc.find(', NV ') >= 0:
        gmt_offset = PST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)
        #modify for daylight savings time:
        if check_DST(local_tim):
            local_tim  = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###OREGON###
    elif loc.find(', OR ') >= 0:
        for z in ['97901','97913','97902','97911','97903','97910','97914','97906','97908','97909','97917','97918','97920']:
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = MST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = PST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###MOUNTAIN###
    elif (loc.find(', CO ') >= 0 or loc.find(', MT ') >= 0 or loc.find(', NM ') >= 0 or loc.find(', UT ') >= 0 or
          loc.find(', WY ') >= 0):
        gmt_offset = MST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)
        #modify for daylight savings time:
        if check_DST(local_tim):
            local_tim  = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###IDAHO###
    elif loc.find(', ID ') >= 0:
        for z in ['83824','83830','83851','83861','83866','83870', #Benewah County
                  '83804','84809','83811','83813','83821','83822','83825','83836','83840','83841','83848','83852','83856', #Bonner County
                  '83860','83864','83865' #Bonner County
                  '83805','83826','83845','83847','83853', #Boundary County
                  '83801','83803','83810','83814','83815','83816','83833','83835','83842','83854','83858','83869', #Kootenai County
                  '83876','83877', #Kootenai County
                  '83535','83537','83806','83823','83832','83834','83843','83844','83855','83857','83871','83872' #Latah County
                  '83523','83536','82543','83548','83555', #Lewis County
                  '83501','83524','83540','83545', #Nez Perce County
                  '83802','83808','83812','83837','83839','83846','83849','83850','83867','83868','83873','83874']: #Shoshone County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = PST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = MST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###EAST###
    elif (loc.find(', CT ') >= 0 or loc.find(', DE ') >= 0 or loc.find(', DC ') >= 0 or loc.find(', GA ') >= 0 or
        loc.find(', ME ') >= 0 or loc.find(', MD ') >= 0 or loc.find(', MA ') >= 0 or loc.find(', NH ') >= 0 or
        loc.find(', NJ ') >= 0 or loc.find(', NY ') >= 0 or loc.find(', NC ') >= 0 or loc.find(', OH ') >= 0 or
        loc.find(', PA ') >= 0 or loc.find(', RI ') >= 0 or loc.find(', SC ') >= 0 or loc.find(', VT ') >= 0 or
        loc.find(', VA ') >= 0 or loc.find(', WV ') >= 0):
        gmt_offset = EST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)
        #modify for daylight savings time:
        if check_DST(local_tim):
            local_tim  = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###FLORIDA###
    elif loc.find(', FL ') >= 0:
        for z in ['32401','32402','32403','32404','32405','32406','32407','32408','32409','32410','32411', #Bay County
                  '32412','32413','32417','32438','32444','32466', #Bay County
            '32421','32424','32430','32499', #Calhoun County
            '32501','32502','32503','32504','32505','32506','32507','32508','32509','32511','32512','32513', #Escambia County
            '32514','32516','32520','32521','32522','32523','32524','32526','32533','32534','32535','32559', #Escambia County
            '32560','32568','32577','32591', #Escambia County
            '32425','32452','32455','32464', #Holmes County
            '32420','32423','32426','32431','32432','32440','32442','32443','32445','32446','32447','32448','32460' #Jackson County
            '32547','32536','32548','32541','32569','32579','32580','32542','32544','32537','32540','32549','32588', #Okaloosa County
            '32566','32571','32570','32583','32565','32530','32561','32562','32563','32572' #Santa Rosa County
            '32422','32433','32434','32435','32439','32459','32461','32538','32550' #Walton County
            '32427','32428','32437','32462','32463']: #Washington County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = CST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = EST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###HAWAII###
    elif loc.find(', HI ') >= 0:
        gmt_offset = HST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###INDIANA###
    elif loc.find(', IN ') >= 0:
        for z in ['46310','46380','46392','47943','47977','47978', #Jasper County
                  '46303','46307','46308','46311','46312','46319','46320','46321','46322','46323','46324','46325','46327', #Lake County
                  '46342','46355','46356','46373','46375','46376','46377','46394','46401','46402','46403','46404','46405', #Lake County
                  '46406','46407','46408','46409','46410','46411', #Lake County
                  '46360','46340','46390','46345','46346','46348','46350','46352','46361','46365','46391','46371','46382' #LaPorte County
                  '46549','46372','46379','46381','47922','47948','47951','47963','47964', #Newton County
                  '46301','46302','46304','46341','46347','46368','46383','46384','46385','46393' #Porter County
                  '46366','46374','46531','46532','46534','46968' #Starke County
                  '47639','47640','47647','47648','47649','47654','47660','47665','47666','47670','47683' #Gibson County
                  '47514','47515','47520','47525','47551','47574','47576','47586' #Perry County
                  '47612','47616','47620','47631','47633','47638', #Posey County
                  '47523','47531','47536','47537','47550','47552','47556','47577','47579','47588','47611','47615','47617','47634','47635' #Spencer County
                  '47618','47701','47702','47703','47704','47705','47706','47708','47710','47711','47712','47713','47714','47715', #Vanderburgh County
                  '47716','47719','47720','47721','47722','47724','47725','47728','47730','47731','47732','47733','47734','47735' #Vanderburgh County
                  '47736','47737','47740','47747','47750' #Vanderburgh County
                  '47601','47610','47613','47619','47629','47630','47637']: #Warrick County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = CST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = EST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###KANSAS###
    elif loc.find(', KS ') >= 0:
        for z in ['66033','66853','67733','67753','67735','67741','67758','67761','67762']:
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = MST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = CST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###KENTUCKY###
    elif loc.find(', KY ') >= 0:
        for z in ['42715','42720','42728','42741','42742','42753', #Adair County
            '42164','42120','42153', #Allen County
            '42123','42127','42130','42131','42141','42142','42152','42156','42160', #Barren County
            '40111','40115','40140','40143','40144','40145','40146','40152','40153','40170','40171','40176','40178', #Breckinridge County
            '42201','42219','42252','42261','42273','42288', #Butler County
            '42020','42036','42049','42054','42071','42076', #Calloway County
            '42021','42023','42035','42070', #Carlisle County
            '42217','42221','42223','42232','42236','42240','42241','42254','42262','42266', #Christian County
            '42602','42603', #Clinton County
            '42033','42037','42064', #Crittendon County
            '42717','42731','42759', #Cumberland County
            '42301','42302','42303','42304','42334','42355','42356','42366','42376','42377','42378', #Daviess County
            '42163','42207','42210','42259','42275','42285', #Edmonson County
            '42041','42050', #Fulton County
            '42027','42039','42040','42051','42061','42063','42066','42069','42079','42082','42085','42088', #Graves County
            '40119','42712','42721','42726','42754','42755','42762', #Grayson County
            '42743','42782', #Green County
            '42348','42351','42364', #Hancock County
            '42713','42722','42729','42746','42749','42765', #Hart County
            '42402','42406','42419','42420','42451','42452','42457','42458', #Henderson County
            '42408','42410','42413','42431','42436','42440','42441','42442','42453','42464', #Hopkins County
            '42028','42045','42047','42058','42078','42081','42083', #Livingston County
            '42202','42206','42256','42265','42276' #Logan County
            '42038','42055' #Lyon County
            '42001','42002','42003','42053','42086' #McCracken County
            '42322','42327','42350','42352','42371','42372', #McLean County
            '42025','42029','42044','42048', #Marshall County
            '42124','42129','42154','42166','42214', #Metcalfe County
            '42133','42140','42151','42157','42167', #Monroe County
            '42321','42323','42324','42325','42326','42330','42332','42337','42339','42344','42345','42367','42374', #Muhlenberg County
            '42320','42328','42333','42338','42343','42347','42349','42354','42361','42368','42369','42370', #Ohio County
            '42629','42642', #Russell County
            '42134','42135', #Simpson County
            '42204','42216','42220','42234','42280','42286', #Todd County
            '42211','42215', #Trigg County
            '42437','42459','42460','42461','42462', #Union County
            '42103','42159','42102','42128', #Warren County
            '42404','42409','42444','42450','42455','42456','42463']: #Webster County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = CST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = EST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###MICHIGAN###
    elif loc.find(', MI ') >= 0:
        for z in ['49911','49938','49947','49959','49968','49969' #Gogebic County
                  '49902','49903','49915','49920','49927','49935','49964' #Iron County
                  '49801','49802','49815','49831','49834','49852','49870','49876','49877','49881','49892' #Dickinson County
                  '49812','49821','49845','49847','49848','49858','49863','49873','49874','49886','49887',
                  '49893','49896']: #Menominee County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = CST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = EST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###NEBRASKA###
    elif loc.find(', NE ') >= 0:
        for z in ['69121', #Arthur County
                  '69345', #Banner County
                  '69301','69348', #Box Butte County
                  '69023','69027','69033','69045', #Chase County
                  '69131','69141','69149','69156','69160','69162', #Cheyenne County
                  '69337','69339','69354','69367', #Dawes County
                  '69122','69129', #Deuel County
                  '69021','69030','69037','69041', #Dundy County
                  '69147','69148','69154','69190', #Garden County
                  '69333','69350','69366', #Grant County
                  '69152', #Hooker County
                  '69127','69144','69146','69153','69155', #Keith County
                  '69128','69133','69145', #Kimball County
                  '69125','69331','69334','69336', #Morrill County
                  '69134','69140','69150','69168', #Perkins County
                  '69341','69352','69353','69355','69356','69357','69358','69361','69363', #Scotts Bluff County
                  '69346']: #Sioux County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = MST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = CST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###NORTH DAKOTA###
    elif loc.find(', ND ') >= 0:
        for z in ['58623', '58651', '58653', #Bowman County
                  '58639', '58649', #Adams County
                  '58620', '58643', #Slope County
                  '58646', '58647', '58650', #Hettinger County
                  '58529', '58533', '58562', '58564', '58569', #Grant County
                  '58601', '58602', '58622', '58630', '58641', '58652', '58655', '58656', #Stark County
                  '58627', '58645', #Billings County
                  '58621', '58632', '58654']: #Golden Valley County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = MST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = CST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###SOUTH DAKOTA###
    elif loc.find(', SD ') >= 0:
        for z in ['57658','57621','57639','57634','57659', #Corson County
                  '57625','57630','57633','57656','57652','57636','57661', #Dewey County
                  '57514','57551','57574', #Bennett County
                  '57762', #Butte County
                  '57722','57730','57738','57744','57773', #Custer County
                  '57735','57747','57763','57766','57782', # Fall River County
                  '57552','57553','57567', #Haakon County
                  '57650','57651','57720','57724','57755','57776', #Harding County
                  '57521','57543','57547','57577','57750', #Jackson County
                  '57732','57754','57759','57779','57783','57793','57799', #Lawrence County
                  '57769','57706','57787','57748','57792','57741','57737', #Meade County
                  '57560','57579','57585', #Mellette County
                  '57701','57702','57703','57709','57719','57725','57745','57751','57761','57767','57775','57780','57790','57791', #Pennington County
                  '57620','57638','57640','57644','57649', #Perkins County
                  '57770','57772','57764','57756','57794','57716', #Shannon County
                  '57532','57537', #Stanley County
                  '57555','57563','57566','57570','57572', #Todd County
                  '57622','57623']: #Ziebach County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = MST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = CST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###TENNESSEE###
    elif loc.find(', TN ') >= 0:
        for z in ['37705','37710','37716','37717','37769','37828','37830','37831', #Anderson County
         '37701','37737','37777','37801','37802','37803','37804','37853','37878','37882','37886', #Blount County
         '37310','37311','37312','37320','37323','37353','37364', #Bradley County
         '37714','37729','37757','37762','37766','37819','37847', #Campbell County
         '37643','37644','37658','37682','37687','37694', #Carter County
         '37707','37715','37724','37730','37752','37773','37824','37825','37851','37867','37870','37879', #Claiborne County
         '37713','37722','37727','37753','37821','37822','37843', #Cocke County
         '37708','37709','37848','37861','37881','37888', #Grainger County
         '37616','37641','37743','37744','37745','37809','37810','37818', #Greene County
         '37778','37813','37814','37815','37816','37860','37877','37891', #Hamblen County
         '37302','37304','37308','37315','37341','37343','37350','37351','37363','37373','37377','37379','37384','37401',
         '37402','37403','37404','37405','37406','37407','37408','37409','37410','37411','37412','37414','37415','37416',
         '37419','37421','37422','37424','37450', #Hamilton County
         '37765','37869', #Hancock County
         '37642','37645','37711','37731','37811','37857','37873', #Hawkins County
         '37725','37760','37820','37871','37890', #Jefferson County
         '37640','37680','37683','37688','37691', #Johnson County
         '37721','37754','37806','37849','37901','37902','37909','37912','37914','37915','37916','37917','37918','37919',
         '37920','37921','37922','37923','37924','37927','37928','37929','37930','37931','37932','37933','37934','37938',
         '37939','37940','37950','37995','37996','37997','37998', #Knox County
         '37742','37771','37772','37774','37846', #Loudon County
         '37303','37309','37329','37331','37370','37371','37826', #McMinn County
         '37322','37336','37880', #Meigs County
         '37314','37354','37385','37874','37885', #Monroe County
         '37719','37726','37733','37770','37829','37845','37872','37887', #Morgan County
         '37307','37316','37317','37325','37326','37333','37361','37362','37369','37391', #Polk County
         '37321','37332','37337','37338','37381', #Rhea County
         '37748','37763','37840','37854', #Roane County
         '37732','37755','37756','37841','37852','37892', #Scott County
         '37738','37764','37862','37863','37864','37865','37868','37876', #Sevier County
         '37617','37618','37620','37621','37625','37660','37662','37663','37664','37665','37669','37686','37699', #Sullivan County
         '37650','37657','37692', #Unicoi County
         '37779','37807','37866', #Union County
         '37601','37602','37604','37605','37614','37615','37656','37659','37681','37684','37690']: #Washington County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = EST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = CST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###TEXAS###
    elif loc.find(', TX ') >= 0:
        for z in ['79821','79835','79836','79838','79849','79853','79901','79902','79903','79904','79905','79906','79907',
                  '79908','79910','79911','79912','79913','79914','79915','79916','79917','79918','79920','79922','79923',
                  '79924','79925','79926','79927','79928','79929','79930','79931','79932','79934','79935','79936','79937',
                  '79938','79940','79941','79942','79943','79944','79945','79946','79947','79948','79949','79950','79951',
                  '79952','79953','79954','79955','79958','79960','79961','79968','79976','79978','79980','79990','79995',
                  '79996','79997','79998','79999','88510','88511','88512','88513','88514','88515','88516','88517','88518',
                  '88519','88520','88521','88523','88524','88525','88526','88527','88528','88529','88530','88531','88532',
                  '88533','88534','88535','88536','88538','88539','88540','88541','88542','88543','88544','88545','88546',
                  '88547','88548','88549','88550','88553','88554','88555','88556','88557','88558','88559','88560','88561',
                  '88562','88563','88565','88566','88567','88568','88569','88570','88571','88572','88573','88574','88575',
                  '88576','88577','88578','88579','88580','88581','88582','88583','88584','88585','88586','88587','88588',
                  '88589','88590','88595', #El Paso County
                  '79837','79839','79847','79851' ]: #Huspedth County
            zipcode_str = ', %s ' % z
            if loc.find(zipcode_str) >= 0:
                gmt_offset = MST_tz
                local_tim  = time.gmtime(tim + gmt_offset*3600)
                #modify for daylight savings time:
                if check_DST(local_tim):
                    local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)
                break
        else:
            gmt_offset = CST_tz
            local_tim  = time.gmtime(tim + gmt_offset*3600)
            #modify for daylight savings time:
            if check_DST(local_tim):
                local_tim = time.gmtime(tim + (1 + gmt_offset)*3600)

    ###AMERICAN SOMOA###
    elif loc.find(', AS ') >= 0:
        gmt_offset = Somoa_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###GUAM###
    elif loc.find(', GU ') >= 0:
        gmt_offset = ChSt_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###NORTHERN MARIANA ISLANDS###
    elif loc.find(', MP ') >= 0:
        gmt_offset = ChSt_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###PUERO RICO###
    elif loc.find(', PR ') >= 0:
        gmt_offset = AST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###VIRGIN ISLANDS###
    elif loc.find(', VI ') >= 0:
        gmt_offset = AST_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###U.S. MINOR OUTLYING ISLANDS###
    elif loc.find(', UM ') >= 0:
        local_tim  = []
        print 'Need greater detail for Minor Outlying Areas'

    ###FEDERATED STATES OF MICRONESIA###
    elif loc.find(', FM ') >= 0:
        gmt_offset = ChSt_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)
        print 'Note that federated states of micronesia have two timezones, so need greater detail about which part.'

    ###MARSHALL ISLANDS###
    elif loc.find(', MH ') >= 0:
        gmt_offset = MHT_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)

    ###PALAU###
    elif loc.find(', PW ') >= 0:
        gmt_offset = Palau_tz
        local_tim  = time.gmtime(tim + gmt_offset*3600)
    return local_tim
