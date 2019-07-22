from update_themes import *

#************************************  ABB RAPID language   **************************************
repository = {}
#------------------------------------



repo_begin_end(repository, "!", r'(?=\n)', name_comment, "comment")
repo_begin_end(repository, r'"', r'"', name_string, "string")
repo_begin_end(repository, r'%', r'%', name_string, "fcn-call")

#match = r'\\b[0-9]\\b'
match = '\\b-?\\d+(\\.\\d*)?([eE][+-]?\\d+)?\\b'
repo_match(repository, match, name_numeric, "numbers")

match = "FOR WHILE FUNC MODULE PROC RECORD TEST TRAP ENDFOR ENDWHILE ENDFUNC ENDMODULE ENDPROC ENDRECORD ENDTEST ENDTRAP"
match += " ALIAS AND BACKWARD CASE CONNECT DEFAULT DIV DO ELSE ELSEIF ENDIF ERROR EXIT FROM GOTO IF INOUT LOCAL MOD NOSTEPIN NOT NOVIEW OR RAISE READONLY RETRY RETURN STEP SYSMODULE THEN TO TRYNEXT UNDO VIEWONLY WITH XOR"
repo_match(repository, match, name_control, "control")

match = "SEARCHC SEARCHEXTJ SEARCHL MOVEABSJ MOVEC MOVECDO MOVECSYNC MOVEEXTJ MOVEJ MOVEJDO MOVEJSYNC MOVEL MOVELDO MOVELSYNC"
repo_match(repository, match, name_movements, "movement")

match = "TRUE FALSE V5 V10 V20 V30 V40 V50 V60 V80 V100 V150 V200 V300 V400 V500 V600 V800 V1000 V1500 V2000 V2500 V3000 V4000 V5000 V6000 V7000 VMAX VROT1 VROT2 VROT5 VROT10 VROT20 VROT50 VROT100 VLIN10 VLIN20 VLIN50 VLIN100 VLIN200 VLIN500 VLIN1000 INPOS20 INPOS50 INPOS100 STOPTIME0_5 STOPTIME1_0 STOPTIME1_5 FLLWTIME0_5 FLLWTIME1_0 FLLWTIME1_5 STR_DIGIT STR_UPPER STR_LOWER STR_WHITE RUN_UNDEF RUN_CONT_CYCLE RUN_INSTR_FWD RUN_INSTR_BWD RUN_SIM RUN_STEP_MOVE OP_UNDEF OP_AUTO OP_MAN_PROG OP_MAN_TEST SPEED TORQUE_REF RESOLVER_ANGLE SPEED_REF DIG_INPUT1 DIG_INPUT2 TOOL0 TP_LATEST WOBJ0 FINE Z0 Z1 Z5 Z10 Z15 Z20 Z30 Z40 Z50 Z60 Z80 Z100 Z150 Z200"
repo_match(repository, match, name_builtInVar, "built-in-var")
match = r'\\On' #regex for \On
repo_match(repository, match, name_builtInVar, "built-in-var")
match = r'\\Off' #regex for \Off
repo_match(repository, match, name_builtInVar, "built-in-var")
match = r'\WD_OUT_\d+' #regex for D_OUT_#
repo_match(repository, match, name_builtInVar, "built-in-var")
match = r'\WD_IN_\d+' #regex for D_IN_#
repo_match(repository, match, name_builtInVar, "built-in-var")
match = r'\\WObj:' #regex for \WObj:
repo_match(repository, match, name_builtInVar, "built-in-var")


match = "ACCSET ACTUNIT ADD ALIASIO BITCLEAR BITSET BOOKERRNO BREAK CALLBYVAR CANCELLOAD CHECKPROGREF CIRPATHMODE CLEAR CLEARIOBUFF CLEARPATH CLEARRAWBYTES CLKRESET CLKSTART CLKSTOP CLOSE CLOSEDIR CONFJ CONFL COPYFILE COPYRAWBYTES CORRCLEAR CORRCON CORRDISCON CORRWRITE DEACTUNIT DECR DITHERACT DITHERDEACT DROPWOBJ EOFFSOFF EOFFSON EOFFSSET ERASEMODULE ERRLOG ERRRAISE ERRWRITE EXITCYCLE GETDATAVAL SETSYSDATA GETTRAPDATA GRIPLOAD HOLLOWWRISTRESET IDELETE IDISABLE IENABLE IERROR INCR INDAMOVE INDCMOVE INDDMOVE INDRESET INDRMOVE INVERTDO IOBUSSTART IOBUSSTATE IODISABLE IOENABLE IPERS IRMQMESSAGE ISIGNALAI ISIGNALAO ISIGNALDI ISIGNALDO ISIGNALGI ISIGNALGO ISLEEP ITIMER IVARVALUE IWATCH LABEL LOAD LOADID MAKEDIR MANLOADIDPROC MECHUNITLOAD MOTIONSUP MTOOLROTCALIB MTOOLTCPCALIB OPEN OPENDIR PACKDNHEADER PACKRAWBYTES PATHACCLIM PATHRECMOVEBWD PATHRECMOVEFWD PATHRECSTART PATHRECSTOP PATHRESOL PDISPOFF PDISPON PDISPSET PROCERRRECOVERY PULSEDO RAISETOUSER READANYBIN READBLOCK READCFGDATA READERRDATA READRAWBYTES REMOVEDIR REMOVEFILE RENAMEFILE RESET RESETPPMOVED RESETRETRYCOUNT RESTOPATH REWIND RMQEMPTYQUEUE RMQFINDSLOT RMQGETMESSAGE RMQGETMSGDATA RMQGETMSGHEADER RMQREADWAIT RMQSENDMESSAGE RMQSENDWAIT SAVE SCWRITE SENDEVICE SET SETALLDATAVAL SETAO SETDATASEARCH SETDATAVAL SETDO SETGO SETSYSDATA SINGAREA SKIPWARN SOCKETACCEPT SOCKETBIND SOCKETCLOSE SOCKETCONNECT SOCKETCREATE SOCKETLISTEN SOCKETRECEIVE SOCKETSEND SOFTACT SOFTDEACT SPEEDREFRESH SPYSTART SPYSTOP STARTLOAD STARTMOVE STARTMOVERETRY STCALIB STCLOSE STEPBWDPATH STINDGUN STINDGUNRESET STOOLROTCALIB STOOLTCPCALIB STOP SUBPROG STOPEN STOPMOVE STOPMOVERESET STOREPATH STTUNE STTUNERESET SYNCMOVEOFF SYNCMOVEON SYNCMOVERESUME SYNCMOVESUSPEND SYNCMOVEUNDO SYSTEMSTOPACTION TESTSIGNDEFINE TESTSIGNRESET TEXTTABINSTALL TPERASE TPREADDNUM TPREADFK TPREADNUM TPSHOW TPWRITE TRIGGC TRIGGCHECKIO TRIGGEQUIP TRIGGINT TRIGGIO TRIGGJ TRIGGL TRIGLIOS TRIGGRAMPAO TRIGGSPEED TRIGGSTOPPROC TRYINT TUNERESET TUNESERVO UIMSGBOX UISHOW UNLOAD UNPACKRAWBYTES VELSET WAITAI WAITAO WAITDI WAITDO WAITGI WAITGO WAITLOAD WAITROB WAITSYNCTASK WAITTESTANDSET WAITTIME WAITUNTIL WAITWOBJ WARMSTART WORLDACCLIM WRITE WRITEANYBIN WRITEBIN WRITEBLOCK WRITECFGDATA WRITERAWBYTES WRITESTRBIN WRITEVAR WZBOXDEF WZCYLDEF WZDISABLE WZDOSET WZENABLE WZFREE WZHOMEJOINTDEF WZLIMJOINTDEF WZLIMSUP WZSPHDEF ABS ABSDNUM ACOS AOUTPUT ARGNAME ASIN ATAN ATAN2 BITAND BITCHECK BITLSH BITNEG BITOR BITRSH BITXOR BYTETOSTR CALCJOINTT CALCROBT CALCROTAXFRAMEZ CALCROTAXISFRAME CDATE CJOINTT CLKREAD CORRREAD COS CPOS CROBT CSPEEDOVERRIDE CTIME CTOOL CWOBJ DECTOHEX DEFACCFRAME DEFDFRAME DIM DISTANCE DNUMTONUM DNUMTOSTR DOTPROD DOUTPUT EULERZYX EVENTTYPE EXECHANDLER EXECLEVEL EXP FILESIZE FILETIME FSSIZE GETMECUNITNAME GETNEXTMECHUNIT GETNEXTSYM GETSERVICEINFO GETSYSINFO GETTASKNAME GETTIME GINPUTDNUM GOUTPUT GOUTPUTDNUM HEXTODEC INDINPOS INDSPEED IOUNITSTATE ISFILE ISMECHUNITACTIVE ISPERS ISSTOPMOVEACT ISSTOPSTATEEVENT ISSYNCMOVEON ISSYSID ISVAR MAXROBSPEED MIRPOS MODEXIST MODTIME MOTIONPLANNERNO NONMOTIONMODE NORIENT NUMTODNUM NUMTOSTR OFFS OPMODE ORIENTZYX OROBT PARIDPOSVALID PARIDROBVALID PATHLEVEL PATHRECVALIDBWD PATHRECVALIDFWD PFRESTART POSEINV POSEMULT POSEVECT POW POWDNUM PPMOVEDINMANMODE PRESENT PROGMEMFREE RAWBYTESLEN READBIN READDIR READMOTOR READNUM READSTR READSTRBIN READVAR RELTOOL REMAININGRETRIES RMQGETSLOTNAME ROBNAME ROBOS ROUND ROUNDDNUM RUNMODE SIN SOCKETGETSTATUS SQRT SQRTDNUM STCALCFORCE STCALCTORQUE STISCALIB STISCLOSED STISINDGUN STISOPEN STRDIGCALC STRDIGCMP STRFIND STRLEN STRMAP STRMATCH STRMEMB STRORDER STRPART STRTOBYTE STRTOVAL TAN TASKRUNMEC TASKRUNROB TASKSINSYNC TESTANDSET TESTDI TESTSIGNREAD TEXTGET TEXTTABFREETOUSE TEXTTABGET TRUNC TRUNCDNUM TYPE UIALPHAENTRY UICLIENTEXIST UIDNUMENTRY UIDNUMTUNE UILISTVIEW UIMESSAGEBOX UINUMENTRY UINUMTUNE VALIDIO VALTOSTR VECTMAGN"
match += " CONST VAR PERS"
repo_match(repository, match, name_builtInFcn, "built-in-fcn")


match = "C_MOTSET C_PROGDISP ERRNO INTNO ROB_ID TUNE_DF TUNE_KP TUNE_KV TUNE_TI TUNE_FRIC_LEV TUNE_FRIC_RAMP TUNE_DG TUNE_DH TUNE_DI TUNE_DK TUNE_DL AIO_ABOVE_HIGH AIO_BELOW_HIGH AIO_ABOVE_LOW AIO_BELOW_LOW AIO_BETWEEN AIO_OUTSIDE AIO_ALWAYS RESUNKWN RESOK RESABORT RESRETRY RESIGNORE RESCANCEL RESYES RESNO BTNNONE BTNOK BTNABRTRTRYIGN BTNOKCANCEL BTNRETRYCANCEL BTNYESNO BTNYESNOCANCEL IOBUS_LOG_STATE_STOPPED IOBUS_LOG_STATE_STARTED IOBUS_PHYS_STATE_HALTED IOBUS_PHYS_STATE_RUNNING IOBUS_PHYS_STATE_ERROR IOBUS_PHYS_STATE_STARTUP IOBUS_PHYS_STATE_INIT BUSSTATE_HALTED BUSSTATE_RUN BUSSTATE_ERROR BUSSTATE_STARTUP BUSSTATE_INIT LOW HIGH EDGE COMMON_ERR OP_STATE SYSTEM_ERR HARDWARE_ERR PROGRAM_ERR MOTION_ERR OPERATOR_ERR IO_COM_ERR USER_DEF_ERR OPTION_PROD_ERR PROCESS_ERR CFG_ERR ERR_ACC_TOO_LOW ERR_ALIASIO_DEF ERR_ALIASIO_TYPE ERR_ALRDYCNT ERR_ALRDY_MOVING ERR_AO_LIM ERR_ARGDUPCND ERR_ARGNAME ERR_ARGNOTPER ERR_ARGNOTVAR ERR_ARGVALERR ERR_AXIS_ACT ERR_AXIS_IND ERR_AXIS_MOVING ERR_AXIS_PAR ERR_BUSSTATE ERR_BWDLIMIT ERR_CALC_NEG ERR_CALC_OVERFLOW ERR_CALC_DIVZERO ERR_CALLPROC ERR_CFG_INTERNAL ERR_CFG_ILLTYPE ERR_CFG_LIMIT ERR_CFG_NOTFND ERR_CFG_OUTOFBOUNDS ERR_CNTNOTVAR ERR_CNV_NOT_ACT ERR_CNV_CONNECT ERR_CNV_DROPPED ERR_COMM_EXT ERR_COMM_INIT_FAILED ERR_DATA_RECV ERR_DEV_MAXTIME ERR_DIPLAG_LIM ERR_DIVZERO ERR_EXECPHR ERR_FILEACC ERR_FILEEXIST ERR_FILEOPEN ERR_FILNOTFND ERR_FNCNORET ERR_FRAME ERR_GO_LIM ERR_ILLDIM ERR_ILLQUAT ERR_ILLRAISE ERR_INDCNV_ORDER ERR_INOISSAFE ERR_INOMAX ERR_INT_NOTVAL ERR_INT_MAXVAL ERR_INVDIM ERR_IODISABLE ERR_IOENABLE ERR_IOERROR ERR_LINKREF ERR_LOADED ERR_LOADID_FATAL ERR_LOADID_RETRY ERR_LOADNO_INUSE ERR_LOADNO_NOUSE ERR_MAXINTVAL ERR_MODULE ERR_MOD_NOTLOADED ERR_NAME_INVALID ERR_NORUNUNIT ERR_NOTARR ERR_NOTEQDIM ERR_NOTINTVAL ERR_NOTPRES ERR_NOTSAVED ERR_NOT_MOVETASK ERR_NUM_LIMIT ERR_OUTOFBND ERR_OVERFLOW ERR_PATH ERR_PATHDIST ERR_PATH_STOP ERR_PID_MOVESTOP ERR_PID_RAISE_PP ERR_PRGMEMFULL ERR_PROCSIGNAL_OFF ERR_PROGSTOP ERR_RANYBIN_CHK ERR_RANYBIN_EOF ERR_RCVDATA ERR_REFUNKDAT ERR_REFUNKFUN ERR_REFUNKPRC ERR_REFUNKTRP ERR_RMQ_DIM ERR_RMQ_FULL ERR_RMQ_INVALID ERR_RMQ_INVMSG ERR_RMQ_MSGSIZE ERR_RMQ_NAME ERR_RMQ_NOMSG ERR_RMQ_TIMEOUT ERR_RMQ_VALUE ERR_ROBLIMIT ERR_SC_WRITE ERR_SIGSUPSEARCH ERR_STARTMOVE ERR_ADDR_INUSE ERR_SOCK_CLOSED ERR_SOCK_TIMEOUT ERR_SPEED_REFRESH_LIM ERR_STRTOOLNG ERR_SYM_ACCESS ERR_SYNCMOVEOFF ERR_SYNCMOVEON ERR_SYNTAX ERR_TASKNAME ERR_TP_DIBREAK ERR_TP_DOBREAK ERR_TP_MAXTIME ERR_TP_NO_CLIENT ERR_TRUSTLEVEL ERR_TXTNOEXIST ERR_UI_INITVALUE ERR_UI_MAXMIN ERR_UI_NOTINT ERR_UISHOW_FATAL ERR_UISHOW_FULL ERR_UNIT_PAR ERR_UNKINO ERR_UNKPROC ERR_UNLOAD ERR_WAITSYNCTASK ERR_WAIT_MAXTIME ERR_WHLSEARCH ERR_WOBJ_MOVING ERRSTR_EMPTY ERRSTR_UNUSED ERRSTR_TASK ERRSTR_CONTEXT TYPE_ALL TYPE_STATE TYPE_WARN TYPE_ERR EVENT_NONE EVENT_POWERON EVENT_START EVENT_STOP EVENT_QSTOP EVENT_RESTART EVENT_RESET EVENT_STEP LEVEL_NORMAL LEVEL_TRAP LEVEL_SERVICE HANDLER_NONE HANDLER_BWD HANDLER_ERR HANDLER_UNDO ICONNONE ICONINFO ICONWARNING ICONERROR IOUNIT_LOG_STATE_DISABLED IOUNIT_LOG_STATE_ENABLED IOUNIT_PHYS_STATE_DEACTIVATED IOUNIT_PHYS_STATE_RUNNING IOUNIT_PHYS_STATE_ERROR IOUNIT_PHYS_STATE_UNCONNECTED IOUNIT_PHYS_STATE_UNCONFIGURED IOUNIT_PHYS_STATE_STARTUP IOUNIT_PHYS_STATE_INIT IOUNIT_RUNNING IOUNIT_RUNERROR IOUNIT_DISABLE IOUNIT_OTHERERR LOAD0 MASS_KNOWN MASS_WITH_AX3 PI OPADD OPSUB OPMULT OPDIV OPMOD LT LTEQ EQ NOTEQ GTEQ GT TOOL_LOAD_ID PAY_LOAD_ID IRBP_K IRBP_L IRBP_C IRBP_C_INDEX IRBP_T IRBP_R IRBP_A IRBP_B IRBP_D ROB_LOAD_VAL ROB_NOT_LOAD_VAL ROB_LM1_LOAD_VAL SOCKET_CREATED SOCKET_CONNECTED SOCKET_BOUND SOCKET_LISTENING SOCKET_CLOSED"
match += " AIOTRIGG BOOL BTNRES BUSSTATE BUTTONDATA BYTE CLOCK CONFDATA CORRDESCR DATAPOS DIONUM DIR DNUM ERRDOMAIN ERRNUM ERRSTR ERRTYPE EVENT_TYPE EXEC_LEVEL EXTJOINT HANDLER_TYPE ICONDATA IDENTNO INTNUM IODEV IOUNIT_STATE JOINTTARGET LISTITEM LOADDATA LOADIDNUM LOADSESSION MECUNIT MOTSETDATA NUM OPCALC OPNUM ORIENT PARIDNUM PARIDVALIDNUM PATHRECID POS POSE PROGDISP RAWBYTES RESTARTDATA RMQHEADER RMQMESSAGE RMQSLOT ROBJOINT ROBTARGET SHAPEDATA SIGNALAI SIGNALAO SIGNALDI SIGNALDO SIGNALGI SIGNALGO SOCKETDEV SOCKETSTATUS SPEEDDATA STOPPOINTDATA STRING STRINGDIG SWITCH SYMNUM SYNCIDENT TASKID TASKS TESTSIGNAL TOOLDATA TPNUM TRAPDATA TRIGGDATA TRIGGIOS TRIGGIOSDNUM TRIGGSTRGO TUNETYPE UISHOWNUM WOBJDATA WZSTATIONARY WZTEMPORARY ZONEDATA"
repo_match(repository, match, name_builtInTypes, "built-in-types")

match = "< >" # &lt;TDN&gt; &lt;DDN&gt; &lt;RDN&gt; &lt;PAR&gt; &lt;ALT&gt; &lt;DIM&gt; &lt;SMT&gt; &lt;VAR&gt; &lt;EIT&gt; &lt;CSE&gt; &lt;EXP&gt; &lt;ARG&gt; &lt;ID&gt; "
repo_match(repository, match, name_operator, "operator")


config_i = dict(default_config)
language_i = {}
language_i["id"] = "ABB"
language_i["aliases"]     = "ABB RAPID S4 S4C IRC5".split(" ")
language_i["extensions"]  = ".sys .mod .prg .pgf".split(" ")
language_i["configuration"] = getFileConfig(language_i["id"])
config_i["comments"] = {"lineComment": "!" }
config_i["folding"] = {
        "markers": {
            "start": r'%%%',
            "end": r'%%%'
        }
    }


print("Updating syntax...")
update_syntax(language_i["id"], repository)

print("Updating configuration...")
update_config(language_i["id"], config_i)

print("Done")

    

















