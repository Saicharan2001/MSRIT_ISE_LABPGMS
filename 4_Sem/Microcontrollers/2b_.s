	AREA PROG2,CODE,READONLY
ENTRY
	MOV R0,#0
	MOV R1,#1
LOOP
	ADD R0,R0,R1
	ADD R1,R1,#2
	CMP R1,#21
	BNE LOOP
GO  B GO
	END