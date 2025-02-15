import { useState, useEffect } from 'react';
import './SearchBar.css';
// State code mapping
const stateCodeMap = {
  'Alabama': 'AL',
  'Arizona': 'AZ',
  'Arkansas': 'AR',
  'California': 'CA',
  'Colorado': 'CO',
  'Connecticut': 'CT',
  'Delaware': 'DE',
  'Florida': 'FL',
  'Georgia': 'GA',
  'Idaho': 'ID',
  'Illinois': 'IL',
  'Indiana': 'IN',
  'Iowa': 'IA',
  'Kansas': 'KS',
  'Kentucky': 'KY',
  'Louisiana': 'LA',
  'Maine': 'ME',
  'Maryland': 'MD',
  'Massachusetts': 'MA',
  'Michigan': 'MI',
  'Minnesota': 'MN',
  'Mississippi': 'MS',
  'Missouri': 'MO',
  'Montana': 'MT',
  'Nebraska': 'NE',
  'Nevada': 'NV',
  'New Hampshire': 'NH',
  'New Jersey': 'NJ',
  'New Mexico': 'NM',
  'New York': 'NY',
  'North Carolina': 'NC',
  'North Dakota': 'ND',
  'Ohio': 'OH',
  'Oklahoma': 'OK',
  'Oregon': 'OR',
  'Pennsylvania': 'PA',
  'Rhode Island': 'RI',
  'South Carolina': 'SC',
  'South Dakota': 'SD',
  'Tennessee': 'TN',
  'Texas': 'TX',
  'Utah': 'UT',
  'Vermont': 'VT',
  'Virginia': 'VA',
  'Washington': 'WA',
  'West Virginia': 'WV',
  'Wisconsin': 'WI',
  'Wyoming': 'WY',
  'District of Columbia': 'DC'
};
const PlacesSearch = ({ onLocationSelect, location, setLocation, isSubmitted, setIsPredictionSelected, setIsInputTyped }) => {
  const [input, setInput] = useState(location);
  const [predictions, setPredictions] = useState([]);
  const [fetching, setFetching] = useState(true);

  // setLocation(input)
  useEffect(() => {
    const runFetch = () => {
      if (input.length >= 2) {
        fetchPredictions(input);
        setIsInputTyped(true);
        setLocation(input)  // Set input typed to true
      } else {
        setPredictions([]);
        if (input.length === 0) {
          setIsInputTyped(false);  // Reset input typed when input is cleared
        }
      }
    }
    runFetch()
  }, [input, fetching, setLocation, setIsInputTyped ]);

  useEffect(() => {
    if (isSubmitted) {
      setPredictions([]);
    }
  }, [isSubmitted]);

  useEffect(() => {
    setInput(location || '');

  }, [location]);

  const fetchPredictions = async (input) => {
    // Special handling for "St." case
    setInput(input)
    if (input.toLowerCase() === 'st' || input.toLowerCase() === 'saint') {
      setPredictions([
        {
          display_name: 'St. Louis Park, MN',
          city: 'St. Louis Park',
          state: 'MN'
        },
        {
          display_name: 'St. Petersburg, FL',
          city: 'St. Petersburg',
          state: 'FL'
        },
        {
          display_name: 'St. Louis, MO',
          city: 'St. Louis',
          state: 'MO'
        }
      ]);
      return;
    }
    //setLocation(input)
    const url = `/api/search/location_search?query=${input}`;

    try {

      const response = await fetch(url);

      if (response.ok) {
        const data = await response.json();
        // if (!location && input.length > 5) {
        //   if (isInputTyped && !isPredictionSelected) {
        //     alert("We aren't there yet! Try another location.");
        //     setInput('')
        //     return;
        //   }
        // }

        setPredictions(
          data.locations
            // .filter(place => place.address.state && place.address.country_code === 'us')
            // .filter(place => !['Alaska', 'Hawaii'].includes(place.address.state))
            // .filter(place => place.address.city || place.address.town || place.address.village) // Ensure there's a city/town/village
            .map(place => {
              let stateCode = stateCodeMap[place.state] || place.state;
              let cityName = place.city;

            //   // Special handling for Washington, DC
            //   if (place.address.state === 'District of Columbia') {
            //     cityName = 'Washington';
            //     stateCode = 'DC';
            //   }

              return {
                display_name: `${cityName}, ${stateCode}`,
                city: cityName,
                state: stateCode
              };
            })
        );
      } else {
        console.error('Error fetching predictions:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching predictions:', error);

    }


  };

  const handleClick = (prediction) => {
    const selectedLocation = `${prediction.city}, ${prediction.state}`;

    setInput(selectedLocation);
    setFetching(false);
    setPredictions([]);
    setIsPredictionSelected(true); // Set prediction selected to true
    onLocationSelect(selectedLocation);
  };

  const handleChange = (e) => {
    setInput(e.target.value);
    setFetching(true);
    setIsPredictionSelected(false); // Reset prediction selected
    setIsInputTyped(true);  // Set input typed to true
    const queryParams = new URLSearchParams();
    queryParams.append('location', input)
  };


  return (
    <div className='location-search-container'>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <input
          type="text"
          value={input}
          onChange={handleChange}
          placeholder="city, state"
          style={{ flex: 1, border: 'none', marginLeft: 10 }}
        />
      </div>
      {predictions?.length > 0 && (
        <div className="predictions-container">
          <ul>
            {predictions.map((prediction, index) => (
              <li className="suggestions" key={index} onClick={() => handleClick(prediction)}>
                {prediction.display_name}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default PlacesSearch;
