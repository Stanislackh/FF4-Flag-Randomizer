"""Liste des flags FF4 FE"""
DicoNomfFlag = {
    1: "DARK SIZE MATTER",
    2: "BLACK OR WHITE",
    3: "LUCK OR NOT",
    4: "STAN'S DREAM",
    5: "TATE NO YUUSHA",
    6: "RUN FOR THE LALAS",
    7: "DRAGON HUNTER",
    8: "KILL THE RELATIVES",
    9: "BOSS RUSH",
    10: "EZ",
    11: "RUN FOR YOUR BOOTY",
}

DicoFlag = {
    # DARK SIZE MATTER FLAG
    "DARK SIZE MATTER": "Omode:dkmatter/win:game Kmain/summon/moon Pkey " \
                        "Cstandard/maybe/start:edward/only:tellah,edward,yang,palom,porom,cid/j:spells,abilities " \
                        "Tstandard/sparse:50 Sstandard Bstandard/alt:gauntlet/whichburn Nchars/key Etoggle/danger " \
                        "Gdupe/life -kit:better",

    # BLACK OR WHITE FLAG
    "BLACK OR WHITE": "Omode:classicgiant/win:game Kmain Pshop Crelaxed/maybe/only:cecil/j:spells,abilities/permajoin "
                      "Tstandard Sstandard Bstandard/alt:gauntlet/whichburn Nchars/key Etoggle "
                      "Gdupe/warp/life -kit:better",

    # LUCK OR NOT
    "LUCK OR NOT": "Orandom:5/win:crystal Kmain/summon/moon Pkey " \
                   "Cstandard/maybe/start:rydia/only:cecil,kain,rydia,rosa,edge,fusoya/j:spells,abilities/permajoin " \
                   "Tstandard/sparse:90 Sstandard Bstandard/alt:gauntlet Nchars/key Etoggle/keep:behemoths " \
                   "Gdupe/warp/life -kit:better",

    # STAN'S DREAM
    "STAN'S DREAM": "Omode:classicgiant/win:crystal Kmain/moon Pkey " \
                    "Crelaxed/maybe/only:porom/j:spells,abilities/permajoin Tstandard Sstandard/free " \
                    "Bstandard/alt:gauntlet/whichburn Nchars/key Etoggle Gdupe/warp/life -kit:better",

    # TATE NO YUUSHA FLAG
    "TATE NO YUUSHA": "Omode:classicforge/win:crystal Kmain/moon Pkey " \
                      "Cstandard/maybe/start:tellah/only:rydia,palom,porom/j:spells,abilities/permajoin " \
                      "Tstandard/sparse:70 Sstandard Bstandard/alt:gauntlet/whichburn Nchars/key " \
                      "Etoggle Gdupe/warp/life -kit:better",

    # RUN FOR THE LALAS FLAG
    "RUN FOR THE LALAS": "O1:quest_dwarfcastle/win:game Kmain Pshop "
                         "Crelaxed/maybe/start:rosa/only:edge/j:spells,abilitiesTstandard Sstandard/free "
                         "Bstandard/whyburn Nnone Etoggle Gdupe/warp/life -kit:better",

    # DRAGON HUNTER FLAG
    "DRAGON HUNTER": "O1:boss_dmist/2:boss_darkelf/3:boss_bahamut/4:boss_paledim/5:boss_wyvern/6:boss_dlunar/win:game " \
                     "Kmain Pnone Crelaxed/maybe/start:kain/j:spells,abilities Twild Swild " \
                     "Bstandard/alt:gauntlet/whichburn Nchars/key Etoggle Gdupe/warp/life -kit:better -spoon",

    # KILL THE RELATIVES FLAG
    "KILL THE RELATIVES": "O1:boss_dmist/2:boss_mirrorcecil/3:boss_golbez/4:boss_kingqueen/win:crystal " \
                          "Kmain/summon/moon Pkey Cstandard/start:rydia/only:cecil,kain,rydia,rosa,edge/" \
                          "j:spells,abilities/nodupes Twild Swild Bstandard/unsafe/alt:gauntlet/whichburn " \
                          "Nnone Etoggle Gwarp/life -kit:better",

    # BOSS RUSH FLAG
    "BOSS RUSH": "Omode:fiends/1:boss_calbrena/2:boss_golbez/3:boss_wyvern/4:boss_plague/5:boss_dlunar/6:boss_odin/" \
                 "7:boss_evilwall/8:boss_mirrorcecil/win:crystal Kmain/summon/moon " \
                 "Pkey Cstandard/maybe/j:spells,abilities/nodupes " \
                 "Twildish Swild/quarter Bstandard/alt:gauntlet/whichburn Nkey Etoggle " \
                 "Gdupe/mp/warp/life -kit:spitball -spoon",

    # EZ
    "EZ": "Omode:classicgiant/win:game Kmain Pshop " \
          "Crelaxed/maybe/start:fusoya/only:cecil,kain,rydia,rosa,porom,edge,fusoya/j:spells,abilities " \
          "Tstandard Sstandard/free Bstandard/alt:gauntlet/whichburn Nnone Etoggle Gdupe/warp/life -kit:better",

    # RUN FOR YOUR BOOTY
    "RUN FOR YOUR BOOTY": "Omode:classicforge/win:crystal Kmain/trap Pshop " \
                          "Crelaxed/maybe/start:edge/only:cecil,kain,rydia,rosa,edge,fusoya/"
                          "j:spells,abilities/permadeath " \
                          "Tstandard/sparse:90 Sstandard Bstandard/alt:gauntlet/whichburn Nchars/key " \
                          "Etoggle/keep:doors,behemoths/danger Gdupe/life -kit:better",

    # ANTI CPU RUN 

}
# Dictionnaire des imges
DicoImages = {
    1: "images/FFIVFE-Characters-5Edward-Active.png",
    2: "images/FFIVFE-Characters-1DKCecil-Active.png",
    3: "images/FFIVFE-Characters-6Rosa-Active.png",
    4: "images/FFIVFE-Characters-8Porom-Active.png",
    5: "images/FFIVFE-Characters-4Tellah-Active.png",
    6: "images/FFIVFE-Characters-3CRydia-Active.png",
    7: "images/FFIVFE-Characters-2Kain-Active.png",
    8: "images/FFIVFE-Bosses-1MistD-Color.png",
    9: "images/FFIVFE-Bosses-36Zeromus-Color.png",
    10: "images/FFIVFE-Characters-11Edge-Active.png",
    11: "images/FFIVFE-Characters-12FuSoYa-Active.png",
    12: "images/timeHasCome.jpg"
}
