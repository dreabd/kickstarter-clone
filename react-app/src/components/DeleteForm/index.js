import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";


const DeleteForm = () => {
  const { closeModal } = useModal()
  const dispatch = useDispatch()

  const deleteProject = (e) => {
    
  }


  return (
    <div >
      <h2>Confirm Delete</h2>
      <button>Yes</button>
      <button onClick={closeModal}>Cancel</button>
    </div>
  )
}


export default DeleteForm
