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
  'Wyoming': 'WY'
};
const PlacesSearch = ({ onLocationSelect, location, isSubmitted, setIsPredictionSelected, setIsInputTyped }) => {
  const [input, setInput] = useState(location);
  const [predictions, setPredictions] = useState([]);
  const [fetching, setFetching] = useState(true);

  useEffect(() => {
    if (fetching && input.length > 0) {
      fetchPredictions(input);
      setIsInputTyped(true);  // Set input typed to true
    } else {
      setPredictions([]);
      if (input.length === 0) {
        setIsInputTyped(false);  // Reset input typed when input is cleared
      }
    }
  }, [input, fetching, setIsInputTyped]);

  useEffect(() => {
    if (isSubmitted) {
      setPredictions([]);
    }
  }, [isSubmitted]);

  useEffect(() => {
    setInput(location || '');
  }, [location]);

  const fetchPredictions = async (input) => {
    const url = `https://nominatim.openstreetmap.org/search?city=${encodeURIComponent(input)}&format=json&addressdetails=1&limit=5`;

    try {
      const response = await fetch(url);

      if (response.ok) {
        const data = await response.json();
        setPredictions(
          data
            .filter(place => place.address.state && place.address.country_code === 'us')
            .filter(place => !['Alaska', 'Hawaii'].includes(place.address.state))
            .filter(place => place.address.city || place.address.town || place.address.village) // Ensure there's a city/town/village
            .map(place => {
              const stateCode = stateCodeMap[place.address.state] || place.address.state;
              const cityName = place.address.city || place.address.town || place.address.village;
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
