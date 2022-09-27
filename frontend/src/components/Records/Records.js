import React, { useEffect, useState } from "react";
import styles from "./records.module.scss";

export default function Records() {

  const [recordsData, setRecordsData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/records")
      .then((response) => response.json())
      .then((data) => {
        setRecordsData(data);
      });
  }, []);

  return (
    <div className={styles.wrapper}>
      <div className={styles.content}>
        
      {recordsData.map((data) => (
          <>
            <>
              <h3>{data.name}</h3>
              <img alt=""src={data.thumbnail} />
              <div class="text">
              <p>{data.abstract}</p>
              </div>
              <p>Country: {data.country}</p>
              <p>Location: {data.location.map((location) => <a href={location}>{location}<br/></a>)}</p>
              {/* {data.founders.map((founder) =>  <p> Founder: <a href={founder}>{founder} </a></p> )} */}
              <p>Founder: {data.founders.map((founder) => <a href={founder}>{founder}<br/></a>)}</p>
            </>
            <hr/>
          </>
        ))}

      </div>
    </div>
  );
}
