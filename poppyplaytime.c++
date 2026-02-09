// A simplified example of grabbing logic
void AGrabPackHand::OnOverlapBegin(UPrimitiveComponent *OverlappedComp, AActor *OtherActor)
{
    if (OtherActor && (OtherActor != this) && OtherActor->IsA(AInteractableProp::StaticClass()))
    {
        // Attach the prop to the hand
        OtherActor->AttachToComponent(HandMesh, FAttachmentTransformRules::KeepWorldTransform);
        bIsHoldingObject = true;

        // Trigger the "creaky" sound effect
        PlaySound(GrabSound);
    }
}