const GetOneList = 'tasks/getOneTask' //done
const GetAllLists = 'tasks/getAllTasks' //done
const CreateList = 'lists/createList' //done
const UpdateList = 'lists/updateList' //done
const DeleteList = 'lists/deleteList' //done

/* -----------ACTION----------- */
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


/* ------------THUNK----------- */
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


  const initialState = {
    allLists: {},
    oneList: {}
  }
  /* ------------REDUCER----------- */
  export default function listsReducer(state = initialState, action) {
    let newState = {};

    switch (action.type) {
        case GetAllLists:
            action.Lists.forEach(List => newState[List.id] = List)
            return newState

        case GetOneList:
          newState = { ...state, oneList: {...state.oneList}}
          newState.oneList = { ...action.list }
          return newState

        case UpdateList:
            newState = { ...state }
            newState[ action.list.id ] = action.list
            return newState

        case DeleteList:
            newState = { ...state }
            delete newState[action.id]
            return newState

        case CreateList:
            newState = { ...state }
            newState[action.list.id] = action.list
            return newState


        default:
            return state
    }
  }
