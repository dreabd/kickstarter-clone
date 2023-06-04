import { useEffect } from 'react';
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getCategoriesThunk } from '../../store/categoryReducer';


function Categories(){
    const dispatch = useDispatch()
	const categories = useSelector(state => state.category.categories);
    console.log("categories", categories)


    useEffect(() => {
        console.log("dispatch")
        dispatch(getCategoriesThunk())
    }, [dispatch])



    if (!categories) return null;
	return (
		<ul>
			{Object.values(categories)?.map(category => {
                return (<li key={category.id}> {category.type} </li>)
            })}

		</ul>
	);
}

export default Categories
