import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom'
import { GetAllListThunk } from "../../store/lists";


const ProfileForm = () => {
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const lists = useSelector(state => state.session.allLists)

  useEffect(() => {
    dispatch(GetAllListThunk())
  }, [dispatch, user])




  return(
    <div>
      <p>{user.username}</p>
      <img src={user.image_url}/>
    </div>
  )
}

export default ProfileForm
