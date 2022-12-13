import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom'
import { GetAllListsThunk } from "../../store/lists";


const ProfileForm = () => {
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const lists = useSelector(state => state.lists)


  useEffect(() => {
    dispatch(GetAllListsThunk())
  }, [dispatch])
  console.log('Object values for list = ',Object.values(lists))

  return(
    <div>
      <p>{user?.username}</p>
      <img src={user?.image_url}/>
      {Object.values(lists).map(list => (
        <div key={list.id}>
          {list.name}
        </div>
      ))}
      <div>follows components</div>
    </div>
  )
}

export default ProfileForm
