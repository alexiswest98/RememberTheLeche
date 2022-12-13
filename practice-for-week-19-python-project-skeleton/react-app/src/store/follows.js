const FOLLOWUSER = 'follows/addFollow'
const UNFOLLOWUSER = 'follows/unfollow'
const GETFOLLOWERS = 'follows/getFollows'
const GETFOLLOWING = 'follows/getFollowing'

export const followAction = (userId) => {
    return {
      type: FOLLOWUSER,
      userId,
    };
  };

  export const unfollowAction = (userId) => {
    return {
      type: UNFOLLOWUSER,
      userId,
    };
  };

  export const getFollowersAction = (currentUser) => {
    return {
      type: GETFOLLOWERS,
      group,
    };
  };

  export const getFollowingAction = (currentUser) => {
    return {
      type: GETFOLLOWING,
      user,
    };
  };


  export const followThunk = (userId) => async (dispatch) => {

    const response = await fetch(`/api/follows/add/${userId}`,
    {
   method: 'POST',
   headers: {'Content-Type':'application/json'},
   body: JSON.stringify({
    followerId: followerId
  })
   })

   if (response.ok) {
    const newFollower = await response.json();
    followAction(newGroup)
     }

  };

  export const unfollowThunk = (followerId) => async (dispatch) => {
    const response = await fetch(`/api/groups/${user_Id}`, {method: 'DELETE'});
    if (response.ok) {
      dispatch(unfollowAction(followerId));
    }
  };

  export const getFollowsThunk = () => async (dispatch) => {
    const response = await fetch(`/api/follows/followers`);
    if (response.ok) {
      const data = await response.json();
      dispatch(getFollowersAction(data));
    }
  };

  export const getFollowingThunk = () => async (dispatch) => {
    const response = await fetch(`/api/follows/following`);
    if (response.ok) {
      const data = await response.json();
      dispatch(getFollowingAction(data));
    }
  };

  export default function followsReducer(state = {}, action){
    let newState = {}
  switch(action.type){

    case FOLLOWUSER:
      newState[action.user.id] = action.user.followers
          return newState

    case UNFOLLOWUSER:
        newState[action.user.id] = action.user.following
            return newState

    case GETFOLLOWERS:
        newState[action.currentUser.id] = action.currentUser.followers
        return newState

    case GETFOLLOWING:
        newState[action.currentUser.id] = action.currentUser.following
        return newState

    default:
        return state
}
}
