from fillpdf import fillpdfs
import os

template_path = "/root/workspace/github.com/CoDanTheBarbarian/5e_character_creator/pdf/Character_Sheet_Template.pdf"
output_path = "/root/workspace/github.com/CoDanTheBarbarian/5e_character_creator/pdf/"

fields_key = {
          'text_1lehv': "name", 
          'text_2doro': "background", 
          'text_3jvjj': "class", 
          'text_4htxk': "race", 
          'text_5fclu': "subclass", 
          'text_6mtop': "level", 
          'text_7bcgp': "xp", 
          'text_8lyot': "ac", 
          'text_9pwko': "current hp", 
          'text_10jsjd': "temp hp", 
          'text_11gboc': "max hp", 
          'text_12mirk': "max hit die", 
          'text_13lfku': "spent hit die", 
          'text_14bhlv': "initiative", 
          'text_15vogh': "speed", 
          'text_16xvdf': "size", 
          'text_17tqcv': "passive perception", 
          'text_18kwvv': "proficiency bonus", 
          'text_19gtct': "strength modifier", 
          'text_20bied': "strength score", 
          'text_21iypl': "intelligence modifer", 
          'text_22pxug': "intelligence score", 
          'text_23asuc': "dexterity modifier", 
          'text_24hmmb': "dexterity score", 
          'text_25ncji': "wisdom modifier", 
          'text_26rbzy': "wisdom score", 
          'text_27qfiv': "constitution modifier", 
          'text_28obur': "constitution score", 
          'text_29zmye': "charisma modifier", 
          'text_30jwsx': "charisma score", 
          'text_31vooh': "acrobatics modifier", 
          'text_32pbxr': "medicine modifier", 
          'text_33tvee': "animal handling modifier", 
          'text_34issc': "arcana modifier", 
          'text_36mpnv': "athletics modifier", 
          'text_37tgqo': "deception modifier", 
          'text_38kvjm': "history modifier", 
          'text_39mmaz': "insight modifier", 
          'text_40vhrl': "intimidation modifier", 
          'text_41lfru': "investigation modifier", 
          'text_42qddx': "nature modifier", 
          'text_44dklr': "perception modifier", 
          'text_45rdl': "performance modifier", 
          'text_46zlii': "persausion modifier", 
          'text_47mtrc': "religion modifier", 
          'text_48wwut': "sleight of hand modifier", 
          'text_49ztsd': "stealth modifier", 
          'text_50fkah': "survival modifier", 
          'text_213vjaj': "weapon 1 name", 
          'text_214lfis': "weapon 2 name", 
          'text_215afnf': "weapon 3 name", 
          'text_216prrs': "weapon 4 name", 
          'text_217iamf': "weapon 5 name", 
          'text_218hjoz': "weapon 6 name", 
          'text_219ameb': "weapon 1 attack bonus/dc", 
          'text_220apjo': "weapon 2 attack bonus/dc", 
          'text_221fixh': "weapon 3 attack bonus/dc", 
          'text_222odvz': "weapon 4 attack bonus/dc", 
          'text_223adiy': "weapon 5 attack bonus/dc", 
          'text_224rbdd': "weapon 6 attack bonus/dc", 
          'text_225fptj': "weapon 1 damage type", 
          'text_226ujth': "weapon 2 damage type", 
          'text_227tuqa': "weapon 3 damage type", 
          'text_228dnel': "weapon 4 damage type", 
          'text_229ftkg': "weapon 5 damage type", 
          'text_230jtwi': "weapon 6 damage type", 
          'text_231piki': "weapon 1 notes", 
          'text_232qdk': "weapon 2 notes", 
          'text_233pfmo': "weapon 3 notes", 
          'text_234zuob': "weapon 4 notes", 
          'text_235akii': "weapon 5 notes", 
          'text_236hoqa': "weapon 6 notes", 
          'textarea_237vdig': "class features box 1", 
          'textarea_238rkrv': "class features box 2", 
          'textarea_239zoqi': "race traits", 
          'textarea_240ngth': "feats", 
          'textarea_245bjob': "tools", 
          'textarea_246zssm': "weapons", 
          'text_247iukc': "constition saving throw", 
          'text_248bhjr': "charisma saving throw", 
          'text_249radr': "wisdom saving throw", 
          'text_250qfah': "dexterity saving throw", 
          'text_251sjko': "strength saving throw", 
          'text_252xwpl': "intelligence saving throw", 
          'checkbox_253xxbz': None, # "strength proficiency", 
          'checkbox_254dvqi': None, # "intelligence proficiency",
          'checkbox_255fxix': None, # "wisdom proficiency",
          'checkbox_256qosr': None, # "dexterity proficiency",
          'checkbox_257yypo': None, # "constitution proficiency",
          'checkbox_258nvba': None, # "charisma proficiency",
          'checkbox_259qthz': None, # "acrobatics proficiency",
          'checkbox_260gwym': None, # "animal handling proficiency", 
          'checkbox_261jsmo': None, # "arcana proficiency",
          'checkbox_262pcmc': None, # "athletics proficiency", 
          'checkbox_263qcjm': None, # "deception proficiency",
          'checkbox_264mtuo': None, # "history proficiency",
          'checkbox_265jdcj': None, # "insight proficiency",
          'checkbox_266dqtq': None, # "intimidation proficiency",
          'checkbox_267oon': None, # "investigation proficiency",
          'checkbox_268hgzb': None, # "medicine proficiency",
          'checkbox_269gfuh': None, # "nature proficiency",
          'checkbox_270sldd': None, # "perception proficiency",
          'checkbox_271zckg': None, # "performance proficiency",
          'checkbox_272klip': None, # "persuasion proficiency",
          'checkbox_273svvi': None, # "religion proficiency",
          'checkbox_274ojmj': None, # "sleight of hand proficiency",
          'checkbox_275jirm': None, # "stealth proficiency",
          'checkbox_276upbq': None, # "survival proficiency",
          'checkbox_277cvsc': None, # "light armor proficiency",
          'checkbox_278xefp': None, # "medium armor proficiency",
          'checkbox_279kstn': None, # "heavy armor proficiency",
          'checkbox_280mvjc': None, # "shield proficiency",
          'checkbox_281mxvf': None, # "death saving throw success 1",
          'checkbox_282phlb': None, # "death saving throw failure 1",
          'checkbox_283zucn': None, # "death saving throw success 2",
          'checkbox_284pedi': None, # "death saving throw failure 2",
          'checkbox_285zjte': None, # "death saving throw success 3",
          'checkbox_286tyof': None, # "death saving throw failure 3",
          'checkbox_415wdfd': None, # "inspiration" 
          'text_51soru': "spellcasting modifier", 
          'text_52xzcj': "spell save dc", 
          'text_53trsa': "spell attack bonus", 
          'text_54owlm': "spell:1 level", 
          'text_55khjy': "spell:2 level", 
          'text_56cqkp': "spell:3 level", 
          'text_57kizl': "spell:4 level", 
          'text_58qbhe': "spell:5 level", 
          'text_59dob': "spell:6 level", 
          'text_60uxsd': "spell:7 level", 
          'text_61aqjt': "spell:8 level", 
          'text_62tfry': "spell:9 level", 
          'text_63sxzn': "spell:10 level", 
          'text_64nsdz': "spell:11 level", 
          'text_65inea': "spell:12 level", 
          'text_66ulko': "spell:13 level", 
          'text_67yciq': "spell:14 level", 
          'text_68liiz': "spell:15 level", 
          'text_69sxis': "spell:16 level", 
          'text_70lywd': "spell:17 level", 
          'text_71nhyk': "spell:18 level", 
          'text_72syfu': "spell:19 level", 
          'text_73iywe': "spell:20 level", 
          'text_74zqxx': "spell:21 level", 
          'text_75nhdb': "spell:22 level", 
          'text_76tcyf': "spell:23 level", 
          'text_77lggp': "spell:24 level", 
          'text_78tif': "spell:25 level", 
          'text_79nnst': "spell:26 level", 
          'text_80zaxi': "spell:27 level", 
          'text_81flxb': "spell:28 level", 
          'text_82jrtf': "spell:29 level", 
          'text_83nwxr': "spell:30 level", 
          'text_84ewwp': "spell:1 casting time", 
          'text_85tc': "spell:2 casting time", 
          'text_86cdpi': "spell:3 casting time", 
          'text_87dktp': "spell:4 casting time", 
          'text_88uwjf': "spell:5 casting time", 
          'text_89vprr': "spell:6 casting time", 
          'text_90slur': "spell:7 casting time", 
          'text_91ucqk': "spell:8 casting time", 
          'text_92evac': "spell:9 casting time", 
          'text_93epci': "spell:10 casting time", 
          'text_94weto': "spell:11 casting time", 
          'text_95xget': "spell:12 casting time", 
          'text_96cipd': "spell:13 casting time", 
          'text_97mlkz': "spell:14 casting time", 
          'text_98olmq': "spell:15 casting time", 
          'text_99mfgo': "spell:16 casting time", 
          'text_100gzjm': "spell:17 casting time",
          'text_101yovg': "spell:18 casting time", 
          'text_102hrxl': "spell:19 casting time", 
          'text_103vhww': "spell:20 casting time", 
          'text_104wwz': "spell:21 casting time", 
          'text_105dfxp': "spell:22 casting time", 
          'text_106naqd': "spell:23 casting time", 
          'text_107tquy': "spell:24 casting time", 
          'text_108nrbs': "spell:25 casting time", 
          'text_109qsjf': "spell:26 casting time", 
          'text_110plzx': "spell:27 casting time", 
          'text_111dpya': "spell:28 casting time", 
          'text_112ilmj': "spell:29 casting time", 
          'text_113vquk': "spell:30 casting time", 
          'text_114qoqr': "spell:1 name", 
          'text_115rugb': "spell:2 name", 
          'text_116hduf': "spell:3 name", 
          'text_117djzw': "spell:4 name", 
          'text_118ippm': "spell:5 name", 
          'text_119fqqs': "spell:6 name", 
          'text_120hyts': "spell:7 name", 
          'text_121rxog': "spell:8 name", 
          'text_122upth': "spell:9 name", 
          'text_123bqjt': "spell:10 name", 
          'text_124cvmw': "spell:11 name", 
          'text_125lray': "spell:12 name", 
          'text_126ogsn': "spell:13 name", 
          'text_127myvj': "spell:14 name", 
          'text_128jljs': "spell:15 name", 
          'text_129eony': "spell:16 name", 
          'text_130xovf': "spell:17 name", 
          'text_131kmf': "spell:18 name", 
          'text_132sdy': "spell:19 name", 
          'text_133qshw': "spell:20 name", 
          'text_134pxnx': "spell:21 name", 
          'text_135zpeh': "spell:22 name", 
          'text_136jowj': "spell:23 name", 
          'text_137lewk': "spell:24 name", 
          'text_138zxvv': "spell:25 name", 
          'text_139bbbo': "spell:26 name", 
          'text_140dlrc': "spell:27 name", 
          'text_141tzdo': "spell:28 name", 
          'text_142vuxp': "spell:29 name", 
          'text_143urgz': "spell:30 name", 
          'text_144xjax': "spell:1 range", 
          'text_145qoyt': "spell:2 range", 
          'text_146nrfg': "spell:3 range", 
          'text_147jgjf': "spell:4 range", 
          'text_148srjj': "spell:5 range", 
          'text_149nhcb': "spell:6 range", 
          'text_150xnzb': "spell:7 range", 
          'text_151rejf': "spell:8 range",
          'text_152kkgc': "spell:9 range", 
          'text_153iafo': "spell:10 range", 
          'text_154dlrr': "spell:11 range", 
          'text_155defd': "spell:12 range", 
          'text_156icda': "spell:13 range", 
          'text_157kazy': "spell:14 range", 
          'text_158xhag': "spell:15 range", 
          'text_159wsdw': "spell:16 range", 
          'text_160xhyq': "spell:17 range", 
          'text_161dmdk': "spell:18 range", 
          'text_162ddxw': "spell:19 range", 
          'text_163rgxd': "spell:20 range", 
          'text_164wpn': "spell:21 range", 
          'text_165fhei': "spell:22 range", 
          'text_166vdsf': "spell:23 range", 
          'text_167gyfn': "spell:24 range", 
          'text_168qtyo': "spell:25 range", 
          'text_169akno': "spell:26 range", 
          'text_170gswt': "spell:27 range", 
          'text_171hreg': "spell:28 range", 
          'text_172bse': "spell:29 range", 
          'text_173igxz': "spell:30 range", 
          'text_174vybk': "spell:1 notes", 
          'text_175syga': "spell:2 notes", 
          'text_176ovnl': "spell:3 notes", 
          'text_177apis': "spell:4 notes", 
          'text_178yrri': "spell:5 notes", 
          'text_179zepm': "spell:6 notes", 
          'text_180viwi': "spell:7 notes", 
          'text_181oatm': "spell:8 notes",
          'text_182sibc': "spell:9 notes", 
          'text_183ssns': "spell:10 notes", 
          'text_184zfz': "spell:11 notes", 
          'text_185sttb': "spell:12 notes", 
          'text_186wamj': "spell:13 notes", 
          'text_187npzm': "spell:14 notes", 
          'text_188yyyw': "spell:15 notes", 
          'text_189kbhl': "spell:16 notes", 
          'text_190juoh': "spell:17 notes", 
          'text_191cvvi': "spell:18 notes", 
          'text_192gbqj': "spell:19 notes", 
          'text_193gfag': "spell:20 notes", 
          'text_194rert': "spell:21 notes", 
          'text_195yzuc': "spell:22 notes", 
          'text_196cdrh': "spell:23 notes", 
          'text_197ns': "spell:24 notes", 
          'text_198jtmw': "spell:25 notes", 
          'text_199ccon': "spell:26 notes", 
          'text_200mcnb': "spell:27 notes", 
          'text_201koff': "spell:28 notes", 
          'text_202npow': "spell:29 notes", 
          'text_203dsbx': "spell:30 notes", 
          'text_204qtpv': "magic item attunement slot 1: name", 
          'text_205ripg': "magic item attunement slot 2: name", 
          'text_206tilr': "magic item attunement slot 3: name", 
          'text_207jfes': "copper pieces", 
          'text_208zlpp': "silver pieces", 
          'text_209lziy': "electrum pieces", 
          'text_210hycy': "gold pieces", 
          'text_211gvpa': "platinum pieces", 
          'text_212sxja': "alignment", 
          'textarea_241jbls': "appearance", 
          'textarea_242ttpk': "backstory & personality", 
          'textarea_243xnms': "languages", 
          'textarea_244f': "equipment", 
          'checkbox_287czvv': None, # "magic item attunement slot 1 box",
          'checkbox_288kbbs': None, # "magic item attunement slot 2 box",
          'checkbox_289teda': None, # "magic item attunement slot 3 box",
          'text_290ljfo': "total level 1 spell slots", 
          'text_291hqz': "total level 2 spell slots", 
          'text_292wtyr': "total level 3 spell slots", 
          'text_293irjl': "total level 4 spell slots", 
          'text_294cgul': "total level 5 spell slots", 
          'text_295wrxu': "total level 6 spell slots", 
          'text_296wupa': "total level 7 spell slots", 
          'text_297smxt': "total level 8 spell slots", 
          'text_298hzov': "total level 9 spell slots", 
          'checkbox_302ypbb': None, # "level 1 spell slot expended box 1",
          'checkbox_303twtx': None, # "level 1 spell slot expended box 2",
          'checkbox_304fbul': None, # "level 1 spell slot expended box 3",
          'checkbox_305ydwj': None, # "level 1 spell slot expended box 4",
          'checkbox_306jlxu': None, # "level 2 spell slot expended box 1",
          'checkbox_307eqvf': None, # "level 2 spell slot expended box 2",
          'checkbox_308xpjq': None, # "level 2 spell slot expended box 3",
          'checkbox_309xarm': None, # "level 3 spell slot expended box 1",
          'checkbox_310ntsi': None, # "level 3 spell slot expended box 2",
          'checkbox_311vjaj': None, # "level 3 spell slot expended box 3",
          'checkbox_312tmpj': None, # "level 4 spell slot expended box 1",
          'checkbox_313sdk': None, # "level 5 spell slot expended box 1",
          'checkbox_314djdf': None, # "level 6 spell slot expended box 1",
          'checkbox_315swrj': None, # "level 4 spell slot expended box 2",
          'checkbox_316dilg': None, # "level 5 spell slot expended box 2",
          'checkbox_317xdas': None, # "level 6 spell slot expended box 2",
          'checkbox_318lwe': None, # "level 4 spell slot expended box 3",
          'checkbox_319eafy': None, # "level 5 spell slot expended box 3",
          'checkbox_320yuqi': None, # "level 7 spell slot expended box 1",
          'checkbox_321byqj': None, # "level 7 spell slot expended box 2",
          'checkbox_322nezk': None, # "level 8 spell slot expended box", 
          'checkbox_323wdjg': None, # "level 9 spell slot expended box",
          'checkbox_324ibcg': None, # "spell:1 concentration",
          'checkbox_325qgob': None, # "spell:1 ritual",
          'checkbox_326pnvo': None, # "spell:1 material", 
          'checkbox_327akxy': None, # "spell:2 concentration", 
          'checkbox_328nffs': None, # "spell:2 ritual",
          'checkbox_329cxii': None, # "spell:3 concentration", 
          'checkbox_330sktt': None, # "spell:3 ritual",
          'checkbox_331uphf': None, # spell:3 material",
          'checkbox_332qbqn': None, # spell:2 material", 
          'checkbox_333dwmp': None, # "spell:4 concentration", 
          'checkbox_334lwxr': None, # "spell:5 concentration", 
          'checkbox_335fezy': None, # "spell:6 concentration",
          'checkbox_336esjj': None, # "spell:7 concentration",
          'checkbox_337gseq': None, # "spell:8 concentration",
          'checkbox_338uftr': None, # "spell:9 concentration", 
          'checkbox_339amyj': None, # "spell:10 concentration", 
          'checkbox_340svcj': None, # "spell:11 concentration", 
          'checkbox_341nltz': None, # "spell:12 concentration", 
          'checkbox_343beuq': None, # "spell:13 concentration", 
          'checkbox_344gdzh': None, # "spell:14 concentration",
          'checkbox_345haat': None, # "spell:15 concentration", 
          'checkbox_346ptis': None, # "spell:16 concentration",
          'checkbox_347kknk': None, # "spell:17 concentration",
          'checkbox_348lqhd': None, # "spell:18 concentration",
          'checkbox_349iogu': None, # "spell:19 concentration",
          'checkbox_350imcb': None, # "spell:20 concentration",
          'checkbox_351izgz': None, # "spell:21 concentration", 
          'checkbox_352duwl': None, # "spell:22 concentration",
          'checkbox_353pzqr': None, # "spell:23 concentration", 
          'checkbox_354aun': None, # "spell:24 concentration", 
          'checkbox_355rawb': None, # "spell:25 concentration",
          'checkbox_356bauz': None, # "spell:26 concentration",
          'checkbox_357fqod': None, # "spell:27 concentration",
          'checkbox_358cpt': None, # "spell:28 concentration",
          'checkbox_359mlnn': None, # "spell:29 concentration",
          'checkbox_360qtas': None, # "spell:30 concentration",
          'checkbox_361aoog': None, # "spell:4 ritual",
          'checkbox_362jvgv': None, # "spell:4 material", 
          'checkbox_363fbqv': None, # "spell:5 ritual",
          'checkbox_364udcu': None, # "spell:5 material",
          'checkbox_365ggjx': None, # "spell:6 ritual",
          'checkbox_366chyp': None, # "spell:6 material",
          'checkbox_367lxqe': None, # "spell:7 ritual",
          'checkbox_368amxh': None, # "spell:7 material",
          'checkbox_369qezs': None, # "spell:8 ritual",
          'checkbox_370tcar': None, # "spell:8 material",
          'checkbox_371ghv': None, # "spell:9 ritual",
          'checkbox_372quix': None, # "spell:9 material",
          'checkbox_373ifgn': None, # "spell:10 ritual", 
          'checkbox_374ietr': None, # "spell:10 material",
          'checkbox_375jtmc': None, # "spell:11 ritual",
          'checkbox_376ofhc': None, # "spell:11 material",
          'checkbox_377xewk': None, # "spell:12 ritual",
          'checkbox_378ftqw': None, # "spell:12 material",
          'checkbox_379cunr': None, # "spell:13 ritual",
          'checkbox_380bpjz': None, # "spell:13 material",
          'checkbox_381bdvq': None, # "spell:14 ritual",
          'checkbox_382ilds': None, # "spell:14 material",
          'checkbox_383aztt': None, # "spell:15 ritual",
          'checkbox_384kiug': None, # "spell:15 material",
          'checkbox_385wltr': None, # "spell:16 ritual",
          'checkbox_386bfgm': None, # "spell:16 material",
          'checkbox_387tbzz': None, # "spell:17 ritual",
          'checkbox_388jpp': None, # "spell:17 material",
          'checkbox_389yptt': None, # "spell:18 ritual",
          'checkbox_390dwxa': None, # "spell:18 material",
          'checkbox_391qnol': None, # "spell:19 ritual",
          'checkbox_392ttth': None, # "spell:19 material",
          'checkbox_393eaol': None, # "spell:20 ritual",
          'checkbox_394msib': None, # "spell:20 material",
          'checkbox_395dnoz': None, # "spell:21 ritual",
          'checkbox_396febm': None, # "spell:21 material",
          'checkbox_397nmbx': None, # "spell:22 ritual",
          'checkbox_398ydzu': None, # "spell:22 material",
          'checkbox_399egyd': None, # "spell:23 ritual",
          'checkbox_400epdl': None, # "spell:23 material",
          'checkbox_401wzuj': None, # "spell:24 ritual",
          'checkbox_402xdcv': None, # "spell:24 material",
          'checkbox_403mavz': None, # "spell:25 ritual",
          'checkbox_404exod': None, # "spell:25 material",
          'checkbox_405uxgy': None, # "spell:26 ritual",
          'checkbox_406lfag': None, # "spell:26 material",
          'checkbox_407exmq': None, # "spell:27 ritual",
          'checkbox_408yann': None, # "spell:27 material",
          'checkbox_409ixpd': None, # "spell:28 ritual",
          'checkbox_410waaf': None, # "spell:28 material", 
          'checkbox_411fxga': None, # "spell:29 ritual",
          'checkbox_412mkmq': None, # "spell:29 material",
          'checkbox_413obqz': None, # "spell:30 ritual",
          'checkbox_414kfjp': None # "spell:30 material"
          }


checkbox_yes_values = {
    'checkbox_253xxbz': 'Yes_sslz', 
    'checkbox_254dvqi': 'Yes_sslz', 
    'checkbox_255fxix': 'Yes_sslz', 
    'checkbox_256qosr': 'Yes_sslz', 
    'checkbox_257yypo': 'Yes_sslz', 
    'checkbox_258nvba': 'Yes_sslz', 
    'checkbox_259qthz': 'Yes_sslz', 
    'checkbox_260gwym': 'Yes_sslz', 
    'checkbox_261jsmo': 'Yes_sslz', 
    'checkbox_262pcmc': 'Yes_sslz', 
    'checkbox_263qcjm': 'Yes_sslz', 
    'checkbox_264mtuo': 'Yes_sslz', 
    'checkbox_265jdcj': 'Yes_sslz', 
    'checkbox_266dqtq': 'Yes_sslz', 
    'checkbox_267oon': 'Yes_sslz', 
    'checkbox_268hgzb': 'Yes_sslz', 
    'checkbox_269gfuh': 'Yes_sslz', 
    'checkbox_270sldd': 'Yes_sslz', 
    'checkbox_271zckg': 'Yes_sslz', 
    'checkbox_272klip': 'Yes_sslz', 
    'checkbox_273svvi': 'Yes_sslz', 
    'checkbox_274ojmj': 'Yes_sslz', 
    'checkbox_275jirm': 'Yes_sslz', 
    'checkbox_276upbq': 'Yes_sslz', 
    'checkbox_277cvsc': 'Yes_sslz', 
    'checkbox_278xefp': 'Yes_sslz', 
    'checkbox_279kstn': 'Yes_sslz', 
    'checkbox_280mvjc': 'Yes_sslz', 
    'checkbox_281mxvf': 'Yes_sslz', 
    'checkbox_282phlb': 'Yes_sslz', 
    'checkbox_283zucn': 'Yes_sslz', 
    'checkbox_284pedi': 'Yes_sslz', 
    'checkbox_285zjte': 'Yes_sslz', 
    'checkbox_286tyof': 'Yes_sslz', 
    'checkbox_415wdfd': 'Yes_ahzd', 
    'checkbox_287czvv': 'Yes_sslz', 
    'checkbox_288kbbs': 'Yes_sslz', 
    'checkbox_289teda': 'Yes_sslz', 
    'checkbox_302ypbb': 'Yes_vriv', 
    'checkbox_303twtx': 'Yes_vriv', 
    'checkbox_304fbul': 'Yes_vriv', 
    'checkbox_305ydwj': 'Yes_vriv', 
    'checkbox_306jlxu': 'Yes_vriv', 
    'checkbox_307eqvf': 'Yes_vriv', 
    'checkbox_308xpjq': 'Yes_vriv', 
    'checkbox_309xarm': 'Yes_vriv', 
    'checkbox_310ntsi': 'Yes_vriv', 
    'checkbox_311vjaj': 'Yes_vriv', 
    'checkbox_312tmpj': 'Yes_vriv', 
    'checkbox_313sdk': 'Yes_vriv', 
    'checkbox_314djdf': 'Yes_vriv', 
    'checkbox_315swrj': 'Yes_vriv', 
    'checkbox_316dilg': 'Yes_vriv', 
    'checkbox_317xdas': 'Yes_vriv', 
    'checkbox_318lwe': 'Yes_vriv', 
    'checkbox_319eafy': 'Yes_vriv',
    'checkbox_320yuqi': 'Yes_vriv', 
    'checkbox_321byqj': 'Yes_vriv', 
    'checkbox_322nezk': 'Yes_vriv', 
    'checkbox_323wdjg': 'Yes_vriv', 
    'checkbox_324ibcg': 'Yes_rqlb', 
    'checkbox_325qgob': 'Yes_rqlb', 
    'checkbox_326pnvo': 'Yes_rqlb', 
    'checkbox_327akxy': 'Yes_rqlb', 
    'checkbox_328nffs': 'Yes_rqlb', 
    'checkbox_329cxii': 'Yes_rqlb', 
    'checkbox_330sktt': 'Yes_rqlb', 
    'checkbox_331uphf': 'Yes_rqlb', 
    'checkbox_332qbqn': 'Yes_rqlb', 
    'checkbox_333dwmp': 'Yes_rqlb', 
    'checkbox_334lwxr': 'Yes_rqlb', 
    'checkbox_335fezy': 'Yes_rqlb', 
    'checkbox_336esjj': 'Yes_rqlb', 
    'checkbox_337gseq': 'Yes_rqlb', 
    'checkbox_338uftr': 'Yes_rqlb', 
    'checkbox_339amyj': 'Yes_rqlb', 
    'checkbox_340svcj': 'Yes_rqlb', 
    'checkbox_341nltz': 'Yes_rqlb', 
    'checkbox_343beuq': 'Yes_rqlb', 
    'checkbox_344gdzh': 'Yes_rqlb', 
    'checkbox_345haat': 'Yes_rqlb', 
    'checkbox_346ptis': 'Yes_rqlb', 
    'checkbox_347kknk': 'Yes_rqlb', 
    'checkbox_348lqhd': 'Yes_rqlb', 
    'checkbox_349iogu': 'Yes_rqlb', 
    'checkbox_350imcb': 'Yes_rqlb', 
    'checkbox_351izgz': 'Yes_rqlb', 
    'checkbox_352duwl': 'Yes_rqlb', 
    'checkbox_353pzqr': 'Yes_rqlb', 
    'checkbox_354aun': 'Yes_rqlb', 
    'checkbox_355rawb': 'Yes_rqlb', 
    'checkbox_356bauz': 'Yes_rqlb', 
    'checkbox_357fqod': 'Yes_rqlb', 
    'checkbox_358cpt': 'Yes_rqlb', 
    'checkbox_359mlnn': 'Yes_rqlb', 
    'checkbox_360qtas': 'Yes_rqlb', 
    'checkbox_361aoog': 'Yes_rqlb', 
    'checkbox_362jvgv': 'Yes_rqlb', 
    'checkbox_363fbqv': 'Yes_rqlb', 
    'checkbox_364udcu': 'Yes_rqlb', 
    'checkbox_365ggjx': 'Yes_rqlb', 
    'checkbox_366chyp': 'Yes_rqlb', 
    'checkbox_367lxqe': 'Yes_rqlb', 
    'checkbox_368amxh': 'Yes_rqlb', 
    'checkbox_369qezs': 'Yes_rqlb', 
    'checkbox_370tcar': 'Yes_rqlb', 
    'checkbox_371ghv': 'Yes_rqlb', 
    'checkbox_372quix': 'Yes_rqlb', 
    'checkbox_373ifgn': 'Yes_rqlb', 
    'checkbox_374ietr': 'Yes_rqlb', 
    'checkbox_375jtmc': 'Yes_rqlb', 
    'checkbox_376ofhc': 'Yes_rqlb', 
    'checkbox_377xewk': 'Yes_rqlb', 
    'checkbox_378ftqw': 'Yes_rqlb', 
    'checkbox_379cunr': 'Yes_rqlb', 
    'checkbox_380bpjz': 'Yes_rqlb', 
    'checkbox_381bdvq': 'Yes_rqlb', 
    'checkbox_382ilds': 'Yes_rqlb', 
    'checkbox_383aztt': 'Yes_rqlb', 
    'checkbox_384kiug': 'Yes_rqlb', 
    'checkbox_385wltr': 'Yes_rqlb', 
    'checkbox_386bfgm': 'Yes_rqlb', 
    'checkbox_387tbzz': 'Yes_rqlb', 
    'checkbox_388jpp': 'Yes_rqlb', 
    'checkbox_389yptt': 'Yes_rqlb', 
    'checkbox_390dwxa': 'Yes_rqlb', 
    'checkbox_391qnol': 'Yes_rqlb', 
    'checkbox_392ttth': 'Yes_rqlb', 
    'checkbox_393eaol': 'Yes_rqlb', 
    'checkbox_394msib': 'Yes_rqlb', 
    'checkbox_395dnoz': 'Yes_rqlb', 
    'checkbox_396febm': 'Yes_rqlb', 
    'checkbox_397nmbx': 'Yes_rqlb', 
    'checkbox_398ydzu': 'Yes_rqlb', 
    'checkbox_399egyd': 'Yes_rqlb', 
    'checkbox_400epdl': 'Yes_rqlb', 
    'checkbox_401wzuj': 'Yes_rqlb', 
    'checkbox_402xdcv': 'Yes_rqlb', 
    'checkbox_403mavz': 'Yes_rqlb', 
    'checkbox_404exod': 'Yes_rqlb', 
    'checkbox_405uxgy': 'Yes_rqlb', 
    'checkbox_406lfag': 'Yes_rqlb', 
    'checkbox_407exmq': 'Yes_rqlb', 
    'checkbox_408yann': 'Yes_rqlb', 
    'checkbox_409ixpd': 'Yes_rqlb', 
    'checkbox_410waaf': 'Yes_rqlb', 
    'checkbox_411fxga': 'Yes_rqlb', 
    'checkbox_412mkmq': 'Yes_rqlb', 
    'checkbox_413obqz': 'Yes_rqlb', 
    'checkbox_414kfjp': 'Yes_rqlb'
    }

zeroed_data = {'text_1lehv': None, 'text_2doro': None, 'text_3jvjj': None, 'text_4htxk': None, 'text_5fclu': None, 'text_6mtop': None, 'text_7bcgp': None, 'text_8lyot': None, 'text_9pwko': None, 'text_10jsjd': None, 'text_11gboc': None, 'text_12mirk': None, 'text_13lfku': None, 'text_14bhlv': None, 'text_15vogh': None, 'text_16xvdf': None, 'text_17tqcv': None, 'text_18kwvv': None, 'text_19gtct': None, 'text_20bied': None, 'text_21iypl': None, 'text_22pxug': None, 'text_23asuc': None, 'text_24hmmb': None, 'text_25ncji': None, 'text_26rbzy': None, 'text_27qfiv': None, 'text_28obur': None, 'text_29zmye': None, 'text_30jwsx': None, 'text_31vooh': None, 'text_32pbxr': None, 'text_33tvee': None, 'text_34issc': None, 'text_36mpnv': None, 'text_37tgqo': None, 'text_38kvjm': None, 'text_39mmaz': None, 'text_40vhrl': None, 'text_41lfru': None, 'text_42qddx': None, 'text_44dklr': None, 'text_45rdl': None, 'text_46zlii': None, 'text_47mtrc': None, 'text_48wwut': None, 'text_49ztsd': None, 'text_50fkah': None, 'text_213vjaj': None, 'text_214lfis': None, 'text_215afnf': None, 'text_216prrs': None, 'text_217iamf': None, 'text_218hjoz': None, 'text_219ameb': None, 'text_220apjo': None, 'text_221fixh': None, 'text_222odvz': None, 'text_223adiy': None, 'text_224rbdd': None, 'text_225fptj': None, 'text_226ujth': None, 'text_227tuqa': None, 'text_228dnel': None, 'text_229ftkg': None, 'text_230jtwi': None, 'text_231piki': None, 'text_232qdk': None, 'text_233pfmo': None, 'text_234zuob': None, 'text_235akii': None, 'text_236hoqa': None, 'textarea_237vdig': None, 'textarea_238rkrv': None, 'textarea_239zoqi': None, 'textarea_240ngth': None, 'textarea_245bjob': None, 'textarea_246zssm': None, 'text_247iukc': None, 'text_248bhjr': None, 'text_249radr': None, 'text_250qfah': None, 'text_251sjko': None, 'text_252xwpl': None, 'checkbox_253xxbz': None, 'checkbox_254dvqi': None, 'checkbox_255fxix': None, 'checkbox_256qosr': None, 'checkbox_257yypo': None, 'checkbox_258nvba': None, 'checkbox_259qthz': None, 'checkbox_260gwym': None, 'checkbox_261jsmo': None, 'checkbox_262pcmc': None, 'checkbox_263qcjm': None, 'checkbox_264mtuo': None, 'checkbox_265jdcj': None, 'checkbox_266dqtq': None, 'checkbox_267oon': None, 'checkbox_268hgzb': None, 'checkbox_269gfuh': None, 'checkbox_270sldd': None, 'checkbox_271zckg': None, 'checkbox_272klip': None, 'checkbox_273svvi': None, 'checkbox_274ojmj': None, 'checkbox_275jirm': None, 'checkbox_276upbq': None, 'checkbox_277cvsc': None, 'checkbox_278xefp': None, 'checkbox_279kstn': None, 'checkbox_280mvjc': None, 'checkbox_281mxvf': None, 'checkbox_282phlb': None, 'checkbox_283zucn': None, 'checkbox_284pedi': None, 'checkbox_285zjte': None, 'checkbox_286tyof': None, 'checkbox_415wdfd': None, 'text_51soru': None, 'text_52xzcj': None, 'text_53trsa': None, 'text_54owlm': None, 'text_55khjy': None, 'text_56cqkp': None, 'text_57kizl': None, 'text_58qbhe': None, 'text_59dob': None, 'text_60uxsd': None, 'text_61aqjt': None, 'text_62tfry': None, 'text_63sxzn': None, 'text_64nsdz': None, 'text_65inea': None, 'text_66ulko': None, 'text_67yciq': None, 'text_68liiz': None, 'text_69sxis': None, 'text_70lywd': None, 'text_71nhyk': None, 'text_72syfu': None, 'text_73iywe': None, 'text_74zqxx': None, 'text_75nhdb': None, 'text_76tcyf': None, 'text_77lggp': None, 'text_78tif': None, 'text_79nnst': None, 'text_80zaxi': None, 'text_81flxb': None, 'text_82jrtf': None, 'text_83nwxr': None, 'text_84ewwp': None, 'text_85tc': None, 'text_86cdpi': None, 'text_87dktp': None, 'text_88uwjf': None, 'text_89vprr': None, 'text_90slur': None, 'text_91ucqk': None, 'text_92evac': None, 'text_93epci': None, 'text_94weto': None, 'text_95xget': None, 'text_96cipd': None, 'text_97mlkz': None, 'text_98olmq': None, 'text_99mfgo': None, 'text_100gzjm': None, 'text_101yovg': None, 'text_102hrxl': None, 'text_103vhww': None, 'text_104wwz': None, 'text_105dfxp': None, 'text_106naqd': None, 'text_107tquy': None, 'text_108nrbs': None, 'text_109qsjf': None, 'text_110plzx': None, 'text_111dpya': None, 'text_112ilmj': None, 'text_113vquk': None, 'text_114qoqr': None, 'text_115rugb': None, 'text_116hduf': None, 'text_117djzw': None, 'text_118ippm': None, 'text_119fqqs': None, 'text_120hyts': None, 'text_121rxog': None, 'text_122upth': None, 'text_123bqjt': None, 'text_124cvmw': None, 'text_125lray': None, 'text_126ogsn': None, 'text_127myvj': None, 'text_128jljs': None, 'text_129eony': None, 'text_130xovf': None, 'text_131kmf': None, 'text_132sdy': None, 'text_133qshw': None, 'text_134pxnx': None, 'text_135zpeh': None, 'text_136jowj': None, 'text_137lewk': None, 'text_138zxvv': None, 'text_139bbbo': None, 'text_140dlrc': None, 'text_141tzdo': None, 'text_142vuxp': None, 'text_143urgz': None, 'text_144xjax': None, 'text_145qoyt': None, 'text_146nrfg': None, 'text_147jgjf': None, 'text_148srjj': None, 'text_149nhcb': None, 'text_150xnzb': None, 'text_151rejf': None, 'text_152kkgc': None, 'text_153iafo': None, 'text_154dlrr': None, 'text_155defd': None, 'text_156icda': None, 'text_157kazy': None, 'text_158xhag': None, 'text_159wsdw': None, 'text_160xhyq': None, 'text_161dmdk': None, 'text_162ddxw': None, 'text_163rgxd': None, 'text_164wpn': None, 'text_165fhei': None, 'text_166vdsf': None, 'text_167gyfn': None, 'text_168qtyo': None, 'text_169akno': None, 'text_170gswt': None, 'text_171hreg': None, 'text_172bse': None, 'text_173igxz': None, 'text_174vybk': None, 'text_175syga': None, 'text_176ovnl': None, 'text_177apis': None, 'text_178yrri': None, 'text_179zepm': None, 'text_180viwi': None, 'text_181oatm': None, 'text_182sibc': None, 'text_183ssns': None, 'text_184zfz': None, 'text_185sttb': None, 'text_186wamj': None, 'text_187npzm': None, 'text_188yyyw': None, 'text_189kbhl': None, 'text_190juoh': None, 'text_191cvvi': None, 'text_192gbqj': None, 'text_193gfag': None, 'text_194rert': None, 'text_195yzuc': None, 'text_196cdrh': None, 'text_197ns': None, 'text_198jtmw': None, 'text_199ccon': None, 'text_200mcnb': None, 'text_201koff': None, 'text_202npow': None, 'text_203dsbx': None, 'text_204qtpv': None, 'text_205ripg': None, 'text_206tilr': None, 'text_207jfes': None, 'text_208zlpp': None, 'text_209lziy': None, 'text_210hycy': None, 'text_211gvpa': None, 'text_212sxja': None, 'textarea_241jbls': None, 'textarea_242ttpk': None, 'textarea_243xnms': None, 'textarea_244f': None, 'checkbox_287czvv': None, 'checkbox_288kbbs': None, 'checkbox_289teda': None, 'text_290ljfo': None, 'text_291hqz': None, 'text_292wtyr': None, 'text_293irjl': None, 'text_294cgul': None, 'text_295wrxu': None, 'text_296wupa': None, 'text_297smxt': None, 'text_298hzov': None, 'checkbox_302ypbb': None, 'checkbox_303twtx': None, 'checkbox_304fbul': None, 'checkbox_305ydwj': None, 'checkbox_306jlxu': None, 'checkbox_307eqvf': None, 'checkbox_308xpjq': None, 'checkbox_309xarm': None, 'checkbox_310ntsi': None, 'checkbox_311vjaj': None, 'checkbox_312tmpj': None, 'checkbox_313sdk': None, 'checkbox_314djdf': None, 'checkbox_315swrj': None, 'checkbox_316dilg': None, 'checkbox_317xdas': None, 'checkbox_318lwe': None, 'checkbox_319eafy': None, 'checkbox_320yuqi': None, 'checkbox_321byqj': None, 'checkbox_322nezk': None, 'checkbox_323wdjg': None, 'checkbox_324ibcg': None, 'checkbox_325qgob': None, 'checkbox_326pnvo': None, 'checkbox_327akxy': None, 'checkbox_328nffs': None, 'checkbox_329cxii': None, 'checkbox_330sktt': None, 'checkbox_331uphf': None, 'checkbox_332qbqn': None, 'checkbox_333dwmp': None, 'checkbox_334lwxr': None, 'checkbox_335fezy': None, 'checkbox_336esjj': None, 'checkbox_337gseq': None, 'checkbox_338uftr': None, 'checkbox_339amyj': None, 'checkbox_340svcj': None, 'checkbox_341nltz': None, 'checkbox_343beuq': None, 'checkbox_344gdzh': None, 'checkbox_345haat': None, 'checkbox_346ptis': None, 'checkbox_347kknk': None, 'checkbox_348lqhd': None, 'checkbox_349iogu': None, 'checkbox_350imcb': None, 'checkbox_351izgz': None, 'checkbox_352duwl': None, 'checkbox_353pzqr': None, 'checkbox_354aun': None, 'checkbox_355rawb': None, 'checkbox_356bauz': None, 'checkbox_357fqod': None, 'checkbox_358cpt': None, 'checkbox_359mlnn': None, 'checkbox_360qtas': None, 'checkbox_361aoog': None, 'checkbox_362jvgv': None, 'checkbox_363fbqv': None, 'checkbox_364udcu': None, 'checkbox_365ggjx': None, 'checkbox_366chyp': None, 'checkbox_367lxqe': None, 'checkbox_368amxh': None, 'checkbox_369qezs': None, 'checkbox_370tcar': None, 'checkbox_371ghv': None, 'checkbox_372quix': None, 'checkbox_373ifgn': None, 'checkbox_374ietr': None, 'checkbox_375jtmc': None, 'checkbox_376ofhc': None, 'checkbox_377xewk': None, 'checkbox_378ftqw': None, 'checkbox_379cunr': None, 'checkbox_380bpjz': None, 'checkbox_381bdvq': None, 'checkbox_382ilds': None, 'checkbox_383aztt': None, 'checkbox_384kiug': None, 'checkbox_385wltr': None, 'checkbox_386bfgm': None, 'checkbox_387tbzz': None, 'checkbox_388jpp': None, 'checkbox_389yptt': None, 'checkbox_390dwxa': None, 'checkbox_391qnol': None, 'checkbox_392ttth': None, 'checkbox_393eaol': None, 'checkbox_394msib': None, 'checkbox_395dnoz': None, 'checkbox_396febm': None, 'checkbox_397nmbx': None, 'checkbox_398ydzu': None, 'checkbox_399egyd': None, 'checkbox_400epdl': None, 'checkbox_401wzuj': None, 'checkbox_402xdcv': None, 'checkbox_403mavz': None, 'checkbox_404exod': None, 'checkbox_405uxgy': None, 'checkbox_406lfag': None, 'checkbox_407exmq': None, 'checkbox_408yann': None, 'checkbox_409ixpd': None, 'checkbox_410waaf': None, 'checkbox_411fxga': None, 'checkbox_412mkmq': None, 'checkbox_413obqz': None, 'checkbox_414kfjp': None}

def get_check_yes_value(checkbox):
    return checkbox_yes_values[checkbox]
# function to populate a new data dictionary with the data from the character sheet
def parse_character_sheet_data(c):
    data = zeroed_data.copy()
    data['text_1lehv'] = c.name
    data['text_2doro'] = c.background
    data['text_3jvjj'] = None # character.class
    data['text_4htxk'] = c.race
    data['text_5fclu'] = None # character.subclass
    data['text_6mtop'] = c.level
    data['text_7bcgp'] = c.xp
    data['text_8lyot'] = c.ac
    data['text_11gboc'] = c.hp
    data['text_12mirk'] = None # c.hit_die
    data['text_14bhlv'] = c.get_ability_score("dexterity")
    data['text_15vogh'] = c.speed
    data['text_17tqcv'] = c.get_skill_bonus("perception")
    data['text_18kwvv'] = c.proficiency_bonus
    data['text_19gtct'] = c.get_ability_score("strength")
    data['text_20bied'] = c.strength
    data['text_21iypl'] = c.get_ability_score("intelligence")
    data['text_22pxug'] = c.intelligence
    data['text_23asuc'] = c.get_ability_score("dexterity")
    data['text_24hmmb'] = c.dexterity
    data['text_25ncji'] = c.get_ability_score("wisdom")
    data['text_26rbzy'] = c.wisdom
    data['text_27qfiv'] = c.get_ability_score("constitution")
    data['text_28obur'] = c.constitution
    data['text_29zmye'] = c.get_ability_score("charisma")
    data['text_30jwsx'] = c.charisma
    data['text_31vooh'] = c.get_skill_bonus("acrobatics")
    data['text_32pbxr'] = c.get_skill_bonus("medicine")
    data['text_33tvee'] = c.get_skill_bonus("animal handling")
    data['text_34issc'] = c.get_skill_bonus("arcana")
    data['text_35ncji'] = c.get_skill_bonus("athletics")
    data['text_36mpnv'] = c.get_skill_bonus("deception")
    data['text_38kvjm'] = c.get_skill_bonus("history") 
    data['text_39mmaz'] = c.get_skill_bonus("insight") 
    data['text_40vhrl'] = c.get_skill_bonus("intimidation") 
    data['text_41lfru'] = c.get_skill_bonus("investigation") 
    data['text_42qddx'] = c.get_skill_bonus("nature") 
    data['text_44dklr'] = c.get_skill_bonus("perception") 
    data['text_45rdl'] = c.get_skill_bonus("performance") 
    data['text_46zlii'] = c.get_skill_bonus("persausion")
    data['text_47mtrc'] = c.get_skill_bonus("religion") 
    data['text_48wwut'] = c.get_skill_bonus("sleight of hand") 
    data['text_49ztsd'] = c.get_skill_bonus("stealth") 
    data['text_50fkah'] = c.get_skill_bonus("survival")
    data['textarea_237vdig'] = None # class features box 1
    data['textarea_238rkrv'] = None # class features box 2
    data['textarea_239zoqi'] = None # race traits
    data['textarea_240ngth'] = None # feats
    data['textarea_245bjob'] = None # tool proficiencies
    data['textarea_246zssm'] = None # weapon proficiencies
    data['text_247iukc'] = c.get_saving_throw("constitutution")
    data['text_248bhjr'] = c.get_saving_throw("charisma") 
    data['text_249radr'] = c.get_saving_throw("wisdom") 
    data['text_250qfah'] = c.get_saving_throw("dexterity")
    data['text_251sjko'] = c.get_saving_throw("strength") 
    data['text_252xwpl'] = c.get_saving_throw("intelligence")
    if c.proficiencies["strength"] == True:
        data['checkbox_253xxbz'] = get_check_yes_value('checkbox_253xxbz')
    if c.proficiencies["intelligence"] == True:
        data['checkbox_254dvqi'] = get_check_yes_value('checkbox_254dvqi')
    if c.proficiencies["wisdom"] == True:
        data['checkbox_255fxix'] = get_check_yes_value('checkbox_255fxix')
    if c.proficiencies["dexterity"] == True:
        data['checkbox_256qosr'] = get_check_yes_value('checkbox_256qosr')
    if c.proficiencies["constitution"] == True:
        data['checkbox_257yypo'] = get_check_yes_value('checkbox_257yypo')
    if c.proficiencies["charisma"] == True:
        data['checkbox_258nvba'] = get_check_yes_value('checkbox_258nvba')
    if c.proficiencies["acrobatics"] == True:
        data['checkbox_259qthz'] = get_check_yes_value('checkbox_259qthz')
    if c.proficiencies["animal handling"] == True:
        data['checkbox_260gwym'] = get_check_yes_value('checkbox_260gwym')
    if c.proficiencies["arcana"] == True:
        data['checkbox_261jsmo'] = get_check_yes_value('checkbox_261jsmo')
    if c.proficiencies["athletics"] == True:
        data['checkbox_262pcmc'] = get_check_yes_value('checkbox_262pcmc')
    if c.proficiencies["deception"] == True:
        data['checkbox_263qcjm'] = get_check_yes_value('checkbox_263qcjm')
    if c.proficiencies["history"] == True:
        data['checkbox_264mtuo'] = get_check_yes_value('checkbox_264mtuo')
    if c.proficiencies["insight"] == True:
        data['checkbox_265jdcj'] = get_check_yes_value('checkbox_265jdcj')
    if c.proficiencies["intimidation"] == True:
        data['checkbox_266dqtq'] = get_check_yes_value('checkbox_266dqtq')
    if c.proficiencies["investigation"] == True:
        data['checkbox_267oon'] = get_check_yes_value('checkbox_267oon')
    if c.proficiencies["medicine"] == True:
        data['checkbox_268hgzb'] = get_check_yes_value('checkbox_268hgzb')
    if c.proficiencies["nature"] == True:
        data['checkbox_269gfuh'] = get_check_yes_value('checkbox_269gfuh')
    if c.proficiencies["perception"] == True:
        data['checkbox_270sldd'] = get_check_yes_value('checkbox_270sldd')
    if c.proficiencies["performance"] == True:
        data['checkbox_271zckg'] = get_check_yes_value('checkbox_271zckg')
    if c.proficiencies["persuasion"] == True:
        data['checkbox_272klip'] = get_check_yes_value('checkbox_272klip')
    if c.proficiencies["religion"] == True:
        data['checkbox_273svvi'] = get_check_yes_value('checkbox_273svvi')
    if c.proficiencies["sleight of hand"] == True:
        data['checkbox_274ojmj'] = get_check_yes_value('checkbox_274ojmj')
    if c.proficiencies["stealth"] == True:
        data['checkbox_275jirm'] = get_check_yes_value('checkbox_275jirm')
    if c.proficiencies["survival"] == True:
        data['checkbox_276upbq'] = get_check_yes_value('checkbox_276upbq')
    if c.proficiencies["light armor"] == True:
        data['checkbox_277cvsc'] = get_check_yes_value('checkbox_277cvsc')
    if c.proficiencies["medium armor"] == True:
        data['checkbox_278xefp'] = get_check_yes_value('checkbox_278xefp')
    if c.proficiencies["heavy armor"] == True:
        data['checkbox_279kstn'] = get_check_yes_value('checkbox_279kstn')
    if c.proficiencies["shield"] == True:
        data['checkbox_280mvjc'] = get_check_yes_value('checkbox_280mvjc')
    data['text_51soru'] = None #spellcasting modifier
    data['text_52xzcj'] = None #spell save dc
    data['text_53trsa'] = None #spell attack bonus
    data['textarea_244f'] = c.inventory

    return data

# fillpdfs.write_fillable_pdfs(template_path, output_path + character_name + ".pdf", character_data)