import { useParams } from "react-router-dom";
import { useDispatch, useSelector} from "react-redux";
import { useEffect, useState } from "react";
import { getUser } from "../../redux/users";
import UserReviews from "./UserReviews";
// import UserSidebar from "./UserSidebar";
import UserOverview from "./Overview";
import UserPhotos from "./UserPhotos";
// import UserBusinesses from "./UserBusinesses";
import "./UserPage.css"
// import { FaUserCircle } from 'react-icons/fa';



function UserPage() {
    const { userId } = useParams();
    // console.log("userId", userId)

    const [currentView, setCurrentView] = useState('overview')

    const dispatch = useDispatch();

    const sessionUser = useSelector(state => (
        state.session.user ? state.session.user : null
    ))

    // console.log("line 21 on user page", sessionUser)

    const viewedUser = useSelector(state => (
        state.users ? state.users[userId] : null
    ))

    // console.log("viewed user", viewedUser)



    useEffect(() => {
        // console.log("useEffect running")
        dispatch(getUser(userId))
    }, [dispatch, userId])



    return (
        <>
            { viewedUser && (
                <div id="full-user-page">

                    <div className="user-sidebar-container">
                        <div className="user-summary-container">
                            {!viewedUser.user_pfp.image_url && (<img className="pfp" id="generic-pfp" src={viewedUser.pfp_url} alt="" />)}
                            {viewedUser.user_pfp.image_url && viewedUser.user_pfp.image_url.length && (<img className="pfp" id='personalized-pfp' src='../../../public/images/defaultAvatar.png' alt="" />)}
                            <h1>{viewedUser.first_name}  {viewedUser.last_name.slice(0,1)}.</h1>
                            <h5>{viewedUser.city}, {viewedUser.state}</h5>
                            <div className="user-summ-stats">
                                <div className="user-summ-stat-item"><i className="fa-solid fa-paw"/>&nbsp;&nbsp;<h5>{viewedUser.num_reviews}</h5></div>&nbsp;&nbsp;&nbsp;&nbsp;
                                <div className="user-summ-stat-item"><i className="fa-solid fa-image"/>&nbsp;&nbsp;<h5>{viewedUser.num_images}</h5></div>
                            </div>
                        </div>
                        <div className="user-navigation-container">
                            <div className="single-user-navigation" onClick={() => {setCurrentView('overview')}}><i className="fa-solid fa-circle-user"/>&nbsp;&nbsp;<h4 className="nav-description">Profile Overview</h4></div>
                            <div className="single-user-navigation" onClick={() => {setCurrentView('reviews')}}><i className="fa-solid fa-paw"/>&nbsp;&nbsp;<h4 className="nav-description">Reviews Written</h4></div>
                            <div className="single-user-navigation" onClick={() => {setCurrentView('photos')}}><i className="fa-solid fa-image"/>&nbsp;&nbsp;<h4 className="nav-description">Photos Added</h4></div>
                        </div>
                    </div>
                    <div className="sub-pages"></div>
                        { currentView == 'overview' && (<div className="sub-page-indiv" id="user-overview-container">
                            <UserOverview/>
                        </div>)}
                        {currentView == 'reviews' && (<div className="sub-page-indiv" id="user-review-container">
                            <UserReviews/>
                        </div>)}
                        {currentView== 'photos' && (<div className="sub-page-indiv" id="user-photo-container">
                            <UserPhotos/>
                        </div>)}
                    </div>
                )
            }
        </>
    )
}

export default UserPage;
