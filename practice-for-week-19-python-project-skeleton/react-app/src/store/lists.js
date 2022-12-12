// import {csrfFetch} from './csrf'

const GetOneList = 'tasks/getOneTask' //done
const GetAllLists = 'tasks/getAllTasks' //done
const CreateList = 'lists/createList' //done
const UpdateList = 'lists/updateList' //done
const DeleteList = 'lists/deleteList' //done

export const GetOneListAction = (list) => {
  return {
    type: GetOneList,
    list
  }
}

export const GetAllListAction = (Lists) => {
  return {
    type: GetAllLists,
    Lists
  }
}

export const CreateListAction = (List) => {
  return{
    type: CreateList,
    List
  }
}

export const UpdateListAction = (List) => {
  return{
    type: UpdateList,
    List
  }
}

export const DeleteListAction = (id) => {
  return{
    type: DeleteList,
    id
  }
}

export const GetOneListThunk = (id) => async (dispatch) => {
  const res = await fetch(`/api/lists/${id}`);
  if (res.ok){
    const data = await res.json();
    dispatch(GetOneListAction(data))
  }
}

export const GetAllListThunk = () => async (dispatch) => {
  const res = await fetch(`/api/lists/all`);
  if (res.ok){
    const data = await res.json();
    dispatch(GetAllListAction(data))
  }
}


export const DeleteListThunk = (list_id) => async (dispatch) => {
  const res = await fetch(`/api/lists/${list_id}`, {method: 'DELETE'});
  if (res.ok){
    const data = await res.json();
    dispatch(DeleteListAction(list_id))
  }
}


export const EditListThunk = (list) => async (dispatch) => {
  const res = await fetch(`/api/lists/${list.id}`, {
    method: 'PUT',
    body: JSON.stringify(list)});
  if (res.ok){
    const data = await res.json()
    dispatch(UpdateListAction(data))
    return data
  }
}

export const CreateListThunk = (list) => async (dispatch) => {
  const res = await fetch(`/api/lists/`, {
    method: 'POST',
    body: JSON.stringify(list)});
  if (res.ok){
    const data = await res.json()
    dispatch(CreateListAction(data))
    return data
  }
}

export default function tasksReducer(state = {}, action) {
  let newState = {};

  switch (action.type) {
      case GetAllLists:
          action.Lists.forEach(list => newState[list.id] = list)
          return newState

      case UpdateList:
          newState = { ...state }
          newState[ action.list.id ] = action.list
          return newState

      case DeleteList:
          newState = { ...state }
          delete newState[action.id]

      case CreateList:
          newState = { ...state }
          newState[action.list.id] = action.list
      default:
          return state
  }
}
