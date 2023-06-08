import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteSingleProjectThunk } from "../../store/projects";
import { getCurrentProjectThunk } from "../../store/projects";

const DeleteForm = ({projectId,setDeleted}) => {
  const { closeModal } = useModal()
  const dispatch = useDispatch()

  console.log(projectId)

  const deleteProject = (e) => {
    dispatch(deleteSingleProjectThunk(projectId))
      .then(setDeleted(true))
      // .then(dispatch(getCurrentProjectThunk()))
      .then(closeModal)
  }


  return (
    <div >
      <h2>Confirm Delete</h2>
      <button onClick={deleteProject}>Yes</button>
      <button onClick={closeModal}>Cancel</button>
    </div>
  )
}


export default DeleteForm
