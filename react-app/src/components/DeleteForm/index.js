import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteSingleProjectThunk } from "../../store/projects";
// import { getCurrentProjectThunk } from "../../store/projects";
import './DeleteForm.css'

const DeleteForm = ({ projectId, setDeleted }) => {
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
    <div className="delete-modal">
      <h2>Are you sure you want to delete this Project?</h2>
      <div className="button-container">
        <button onClick={closeModal}>Cancel</button>
        <button className="delete-button" onClick={deleteProject}>Delete</button>
      </div>
    </div>
  )
}


export default DeleteForm
