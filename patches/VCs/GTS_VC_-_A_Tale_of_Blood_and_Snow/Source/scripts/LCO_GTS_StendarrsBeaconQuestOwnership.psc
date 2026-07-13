Scriptname LCO_GTS_StendarrsBeaconQuestOwnership extends Quest

LCO_GTS_StendarrsBeaconController Property StendarrsBeaconController Auto

Int Property OwnershipStage = 50 Auto
Float Property CheckInterval = 5.0 Auto

Bool ownershipApplied = False


Event OnInit()
	RegisterForSingleUpdate(1.0)
EndEvent


Event OnUpdate()
	CheckOwnership()
EndEvent


Function CheckOwnership()
	If ownershipApplied
		Return
	EndIf

	If GetStage() < OwnershipStage
		RegisterForSingleUpdate(CheckInterval)
		Return
	EndIf

	If StendarrsBeaconController == None
		Debug.Trace("[LCO GTS] Stendarr's Beacon controller property is missing.")
		RegisterForSingleUpdate(30.0)
		Return
	EndIf

	If StendarrsBeaconController.SetVolkiharOwnership()
		ownershipApplied = True
		UnregisterForUpdate()
	Else
		Debug.Trace("[LCO GTS] Failed to apply vampire ownership to Stendarr's Beacon.")
		RegisterForSingleUpdate(30.0)
	EndIf
EndFunction