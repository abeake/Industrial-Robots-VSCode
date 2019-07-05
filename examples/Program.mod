%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_Program

    ! -------------------------------
    ! Define customized variables here
    ! ...
	! Tool variables: 
	PERS tooldata Tool := [TRUE,[[-30.000,0.000,40.000],[0.86602540,0.00000000,-0.50000000,0.00000001]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

	! Reference variables:
	PERS wobjdata Frame2 := [FALSE, TRUE, "", [[399.855,0.000,100.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[[0,0,0],[1,0,0,0]]];
    
	PROC Main()
		ConfJ \On;
		ConfL \Off;
		! Program generated by RoboDK v3.6.2 for ABB IRB 1200-7/0.7 on 27/03/2019 16:52:41
		! Using nominal kinematics.
		MoveAbsJ [[-0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,Tool,\WObj:=Frame2;
		MoveAbsJ [[-0.000000,-3.686624,-0.702897,-0.000000,-56.114712,0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,Tool,\WObj:=Frame2;
		WaitTime 0.500;
		MoveL [[18.715,147.321,458.168],[0.00000000,-0.97969618,0.00000000,0.20048792],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,Tool,\WObj:=WObj0;
		MoveL [[3.281,147.321,294.993],[0.00000000,-0.97969618,0.00000000,0.20048792],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,Tool,\WObj:=Frame2;
		TPWrite "Stop the robot until the user wants to continue";
		! Remove next line to prevent the robot from stopping
		STOP;
		TPWrite "Running program Prog2";
		Subprog;
		MoveL [[3.281,4.678,294.993],[0.00000000,-0.97969618,0.00000000,0.20048792],[0,0,-1,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,Tool,\WObj:=Frame2;
		TPWrite "Set Digital Output 5 to ON";
		SetDO D_OUT_5, 1;
		MoveL [[18.715,0.000,458.168],[0.00000000,-0.97969618,0.00000000,0.20048792],[0,0,0,1],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,Tool,\WObj:=Frame2;
		TPWrite "Wait for digital input 5 to turn ON";
		WaitDI D_IN_5, 1;
	ENDPROC

ENDMODULE
