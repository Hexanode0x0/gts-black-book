Scriptname LCO_GTS_StendarrsBeaconController extends LCO_LocationControllerBase


Message Property ClaimVigilOrDawnguard Auto
{Manual reclaim menu shown when the Beacon is controlled by the vampire clans, the player is cured, and the player has joined the Dawnguard.}

Message Property ClaimVigilOnly Auto
{Manual reclaim menu shown when the Beacon is controlled by the vampire clans and the player has not joined the Dawnguard.}

Message Property NoClaim Auto
{Shown while the player is in combat or the location has not been cleared.}

Message Property VampireLocked Auto
{Shown while the player is currently a vampire.}

Message Property VigilantsHoldBeacon Auto
{Shown when the Beacon is already controlled by the Vigil of Stendarr.}


Actor Property PlayerRef Auto

Keyword Property Vampire Auto
{Vampire [KYWD:000A82BB]}

Quest Property DLC1HunterBaseIntro Auto
{A New Order [QUST:01004E24]. Stage 20 is set when the player follows the Dawnguard branch.}


ObjectReference Property DawnguardMarker Auto
{Enable parent for Dawnguard-owned references.}

ObjectReference Property VolkiharMarker Auto
{Enable parent for ATOBAS/Volkihar-owned references.}

ObjectReference Property VigilantMarker Auto
{Enable parent for Vigilant-owned references.}


Event OnInit()
	If EnsureOwnershipState()
		SyncOwnershipMarkers()
	EndIf
EndEvent


Event OnLoad()
	If EnsureOwnershipState()
		SyncOwnershipMarkers()
	EndIf
EndEvent


Event OnActivate(ObjectReference akActionRef)
	Actor activatingActor = akActionRef as Actor
	Int currentOwner
	Int selectedOwner
	Int selectedChoice = -1

	If PlayerRef == None
		PlayerRef = Game.GetPlayer()
	EndIf

	; Ignore activation by anything other than the player.
	If activatingActor == None || activatingActor != PlayerRef
		Return
	EndIf

	If !EnsureOwnershipState()
		Return
	EndIf

	currentOwner = thisLocation.GetKeywordData(CurrentOwnership) as Int

	; The Beacon is already held by the Vigilants.
	If currentOwner == 16
		ShowConfiguredMessage(VigilantsHoldBeacon, "VigilantsHoldBeacon")
		Return
	EndIf

	; Manual reclaiming is only relevant while the ATOBAS vampire clans
	; control the Beacon through LCO's Volkihar ownership slot.
	If currentOwner != 10
		Return
	EndIf

	If activatingActor.IsInCombat() || !thisLocation.IsCleared()
		ShowConfiguredMessage(NoClaim, "NoClaim")
		Return
	EndIf

	If IsPlayerVampire()
		ShowConfiguredMessage(VampireLocked, "VampireLocked")
		Return
	EndIf

	selectedOwner = currentOwner

	If CanClaimForDawnguard()
		If ClaimVigilOrDawnguard == None
			Debug.Trace("[LCO GTS] Stendarr's Beacon ClaimVigilOrDawnguard message is missing.")
			Return
		EndIf

		selectedChoice = ClaimVigilOrDawnguard.Show()

		If selectedChoice == 0
			selectedOwner = 16 ; Vigil of Stendarr
		ElseIf selectedChoice == 1
			selectedOwner = 9 ; Dawnguard
		EndIf
	Else
		If ClaimVigilOnly == None
			Debug.Trace("[LCO GTS] Stendarr's Beacon ClaimVigilOnly message is missing.")
			Return
		EndIf

		selectedChoice = ClaimVigilOnly.Show()

		If selectedChoice == 0
			selectedOwner = 16 ; Vigil of Stendarr
		EndIf
	EndIf

	If selectedOwner != currentOwner
		; Manual claims use LCO's delayed ownership update.
		newOwner = selectedOwner
		GoToState("UpdateQueued")
	Else
		newOwner = currentOwner
		GoToState("Waiting")
	EndIf
EndEvent


Bool Function CanClaimForDawnguard()
	If DLC1HunterBaseIntro == None
		Debug.Trace("[LCO GTS] Stendarr's Beacon DLC1HunterBaseIntro property is missing.")
		Return False
	EndIf

	; Stage 20 is set when the player proceeds along the Dawnguard branch
	; after refusing Harkon's offer.
	Return DLC1HunterBaseIntro.IsStageDone(20)
EndFunction


Bool Function IsPlayerVampire()
	If PlayerRef == None
		PlayerRef = Game.GetPlayer()
	EndIf

	; Fail closed if a required property is missing.
	If PlayerRef == None
		Debug.Trace("[LCO GTS] Stendarr's Beacon PlayerRef property is missing.")
		Return True
	EndIf

	If Vampire == None
		Debug.Trace("[LCO GTS] Stendarr's Beacon Vampire keyword property is missing.")
		Return True
	EndIf

	Return PlayerRef.HasKeyword(Vampire)
EndFunction


Function ShowConfiguredMessage(Message akMessage, String asPropertyName)
	If akMessage != None
		akMessage.Show()
	Else
		Debug.Trace("[LCO GTS] Stendarr's Beacon " + asPropertyName + " message is missing.")
	EndIf
EndFunction


Bool Function EnsureOwnershipState()
	Int currentOwner

	If thisLocation == None
		Debug.Trace("[LCO GTS] Stendarr's Beacon location property is missing.")
		Return False
	EndIf

	If DefaultOwnership == None
		Debug.Trace("[LCO GTS] DefaultOwnership keyword property is missing.")
		Return False
	EndIf

	If CurrentOwnership == None
		Debug.Trace("[LCO GTS] CurrentOwnership keyword property is missing.")
		Return False
	EndIf

	; Stendarr's Beacon begins under Vigilant ownership.
	defaultOwner = 16
	thisLocation.SetKeywordData(DefaultOwnership, defaultOwner)

	currentOwner = thisLocation.GetKeywordData(CurrentOwnership) as Int

	; Initialize an unset or unsupported ownership value as Vigilant.
	If !IsSupportedOwner(currentOwner)
		currentOwner = defaultOwner
		thisLocation.SetKeywordData(CurrentOwnership, currentOwner)
	EndIf

	newOwner = currentOwner

	Return True
EndFunction


Function SyncOwnershipMarkers()
	Int currentOwner

	If thisLocation == None || CurrentOwnership == None
		Return
	EndIf

	currentOwner = thisLocation.GetKeywordData(CurrentOwnership) as Int

	SetOwnershipMarkerState(DawnguardMarker, currentOwner == 9, "DawnguardMarker")
	SetOwnershipMarkerState(VolkiharMarker, currentOwner == 10, "VolkiharMarker")
	SetOwnershipMarkerState(VigilantMarker, currentOwner == 16, "VigilantMarker")
EndFunction


Function SetOwnershipMarkerState(ObjectReference akMarker, Bool abShouldBeEnabled, String asPropertyName)
	If akMarker == None
		Debug.Trace("[LCO GTS] Stendarr's Beacon " + asPropertyName + " property is missing.")
		Return
	EndIf

	; Only change the marker when its current state is wrong.
	; This avoids unnecessary disable/enable cycles for NPCs and objects.
	If abShouldBeEnabled
		If akMarker.IsDisabled()
			akMarker.EnableNoWait()
		EndIf
	Else
		If !akMarker.IsDisabled()
			akMarker.DisableNoWait()
		EndIf
	EndIf
EndFunction


Bool Function IsSupportedOwner(Int aiOwner)
	If aiOwner == 9
		; Dawnguard
		Return True
	EndIf

	If aiOwner == 10
		; Volkihar ownership slot, also used by the ATOBAS vampire clans.
		Return True
	EndIf

	If aiOwner == 16
		; Vigil of Stendarr
		Return True
	EndIf

	Return False
EndFunction


Bool Function SetOwnership(Int aiOwner)
	Int currentOwner

	If !IsSupportedOwner(aiOwner)
		Debug.Trace("[LCO GTS] Unsupported Stendarr's Beacon owner: " + aiOwner)
		Return False
	EndIf

	If !EnsureOwnershipState()
		Return False
	EndIf

	If ChangeOwnership == None
		Debug.Trace("[LCO GTS] ChangeOwnership keyword property is missing.")
		Return False
	EndIf

	currentOwner = thisLocation.GetKeywordData(CurrentOwnership) as Int

	; If ownership is already correct, repair any stale marker states
	; without sending another ownership event.
	If currentOwner == aiOwner
		newOwner = aiOwner
		SyncOwnershipMarkers()
		Return True
	EndIf

	; Quest-driven ownership changes remain immediate and bypass all
	; manual reclaim conditions.
	newOwner = aiOwner
	UpdateOwnership()

	Return True
EndFunction


Bool Function SetVigilantOwnership()
	Return SetOwnership(16)
EndFunction


Bool Function SetVolkiharOwnership()
	Return SetOwnership(10)
EndFunction


Bool Function SetDawnguardOwnership()
	Return SetOwnership(9)
EndFunction