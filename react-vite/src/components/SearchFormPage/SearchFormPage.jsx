// import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchBusinesses } from "../../redux/search";
import "./SearchForm.css";
import { Link, useLocation } from "react-router-dom";
import FilterComponent from "./FilterComponent";
import { getTodaysHours } from "../../utils";
import { useEffect, useState } from "react";
import { fetchAllBusinesses } from "../../redux/businesses";


function SearchFormPage() {

  const dispatch = useDispatch();
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const category = searchParams.get('category');

  console.log("CATEGORY IN SEARCH PAGE", category)

  const businesses = Object.values(useSelector((state) => state.search.businesses))
  const { total, pages, currentPage, perPage } = useSelector(state => state.search.pagination);
  const [page, setPage] = useState(currentPage);
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 480);
  const [isTablet, setIsTablet] = useState(window.innerWidth <= 768 && window.innerWidth >= 481);

  const handleResize = () => {
    setIsMobile(window.innerWidth <= 480);
    setIsTablet(window.innerWidth <= 768 && window.innerWidth >= 481);
  }

  useEffect(() => {
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize)
  }, []);

  const starReviews = (numStars) => {

    let filledStars = []
    let emptyStars = []

    for (let i = 0; i < parseInt(numStars); i++) {
      filledStars.push(<span className='paws-filled' style={{ fontSize: "large" }}><i className="fa-solid fa-paw" />&nbsp;</span>)
    }
    let empty = 5 - filledStars.length
    for (let i = 0; i < empty; i++) {
      emptyStars.push(<span className='paws-unfilled' style={{ fontSize: "large" }}><i className="fa-solid fa-paw" />&nbsp;</span>)
    }
    return [filledStars, emptyStars]
  }

  const starsToFixed = (stars) => {
    let int = +stars
    if (int >= 1) {
      return int.toFixed(1)
    } else {
      return false
    }
  }


  const reviewsExists = (review) => {
    if (review === 1) {
      return '(' + review + ' ' + 'review' + ')'
    }
    if (review >= 1) {
      return '(' + review + ' ' + 'reviews' + ')'
    }
    return false
  }

  const reviewTextSubstr = (text) => {
    if (text.length > 85) {
      return text.substring(0, 85) + "..."
    } else {
      return text
    }
  }

  const handleFilterChange = (filters) => {
    dispatch(fetchBusinesses(filters, page, perPage))
  }

  useEffect(() => {
    dispatch(fetchBusinesses(businesses, page, perPage))
      .catch(error => {
        return error
      })
  }, [dispatch, businesses, page, perPage])

  const handleNextPage = (e) => {
    e.preventDefault();
    const nextPage = currentPage + 1;
    if (nextPage <= pages) {
      setPage(nextPage);
      dispatch(fetchBusinesses(businesses, nextPage, perPage));
      window.scrollTo(0, 0); // Scroll to top
    }
  };

  const handlePrevPage = (e) => {
    e.preventDefault();
    const prevPage = currentPage - 1;
    if (prevPage >= 1) {
      setPage(prevPage);
      dispatch(fetchAllBusinesses(businesses, prevPage, perPage));
      window.scrollTo(0, 0); // Scroll to top
    }
  };


  return (
    <>
      <div className="searchPage">
        <h1>Paw-Recommended Results:</h1>
        <FilterComponent onFilterChange={handleFilterChange} isMobile={isMobile} isTablet={isTablet} />
        <span>Total Businesses Found: {total}</span>
        {businesses.length === 0 ? (
          <span className="noBiz" >No results found.<img src="/images/icons/404.png" /></span>
        ) : (
          businesses && businesses.map((business, index) => (
            <div className="card" key={business.id}>
              <Link className="businessCards" style={{ textDecoration: "none" }} to={`/businesses/${business.id}`}>

                <span className="businessesImageWrapper">

                  {business.images?.[0] ? (
                    <img className="businessesImage" src={business.images[0]} alt={business.name} />
                  ) : (
                    <img className="businessesImage" src='../../images/default_business.jpeg' alt={business.name} />
                  )}

                </span>

                <>
                  <span className="businessDeets">
                  <h2>{(page - 1) * perPage + index + 1}.&nbsp;{business.name}</h2>
                    {
                      business.avg_stars &&

                      business.num_reviews && reviewsExists(business.num_reviews) &&
                      <span className="searchStars">{business?.avg_stars && starReviews(business.avg_stars)}
                        &nbsp;{business?.avg_stars && starsToFixed(business.avg_stars)}
                        &nbsp;{business.num_reviews >= 1 && reviewsExists(business.num_reviews)}</span>

                    }

                    {!business.price ? (

                      <p className="priceSubcat">{business.category?.name}
                      </p>
                    ) : (
                      <p className="priceSubcat">{business.price} &nbsp;&#183;&nbsp; {business.category?.name}
                      </p>
                    )
                    }

                    {
                      getTodaysHours(business) &&
                      <span className="todayHours">
                        <span style={{ fontWeight: '600' }}>Today&apos;s Hours:</span> {getTodaysHours(business).open} - {getTodaysHours(business).close}
                      </span>
                    }

                    <span className="review-text-wrapper">
                      {business.recent_review_text ?
                        (
                          <div className="recent-review-text">
                            <i className="fa-regular fa-message fa-flip-horizontal" />

                            &nbsp;&nbsp;
                            {business.recent_review_text &&
                              reviewTextSubstr(business.recent_review_text)
                            }
                          </div>
                        ) : (
                          <span><span className='paws-unfilled' style={{ fontSize: "medium" }}><i className="fa-solid fa-paw" /></span>&nbsp;&nbsp;Be the first to review!</span>
                        )}
                    </span>
                  </span>
                </>
              </Link>
            </div>
          ))
        )}
        <div className="pagination">
          <button onClick={handlePrevPage} disabled={currentPage === 1}>Previous</button>
          <span>Page {currentPage} of {pages}</span>
          <button onClick={handleNextPage} disabled={currentPage === pages}>Next</button>
        </div>
      </div>
    </>
  );
}

export default SearchFormPage;
