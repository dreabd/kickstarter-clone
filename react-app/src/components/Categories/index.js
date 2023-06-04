import { useEffect } from 'react';
import react from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getCategoriesThunk } from '../../store/categoryReducer';


function Categories(){
    const dispatch = useDispatch()
	const categories = useSelector(state => state.categories);

    useEffect(() => {
        dispatch(getCategoriesThunk())
    }, [dispatch])

	return (
		<ul>
			{categories.map(category => {
                return (<li key={category.id}> {category.type} </li>)
            })}

		</ul>
	);
}

export default Categories
