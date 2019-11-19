using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MastAgent : Agent
{
    [Header("MastAgent")]
    public GameObject mast;
    public HingeJoint hinge;
    JointSpring spring;

    public override void InitializeAgent()
    {
        hinge = mast.GetComponent<HingeJoint>();
        spring = hinge.spring;
    }

    public override void CollectObservations()
    { 
        AddVectorObs(hinge.angle);
    }

    public override void AgentAction(float[] vectorAction, string textAction)
    {
        spring.targetPosition = vectorAction[0];
        hinge.spring = spring;

        SetReward(Time.time);

        if (hinge.angle < -90 || hinge.angle > 90)
        {    
            Done();
        }


    }

    public override void AgentReset()
    {
        spring.targetPosition = 0;
        hinge.spring = spring;
    }

}
