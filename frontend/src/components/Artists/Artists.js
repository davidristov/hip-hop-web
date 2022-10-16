import React, { useEffect, useState } from "react";
import styles from "./artists.module.scss";

export default function Artists() {
  const [artistData, setArtistData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/artists")
      .then((response) => response.json())
      .then((data) => {
        setArtistData(data);
      });
  }, []);

  return (
    <div className={styles.wrapper}>
      <div className={styles.content}>
        {artistData.map((data) => (
          <>
            <>
              <h3>{data.name}</h3>
              <img alt="" src={data.thumbnail} />
              <p>{data.abstract}</p>
              <p>Birth Date: {data.birthDate}</p>
              <p> Birth Place: <a href={data.birthPlace}>{data.birthPlace}</a></p>
              <p>Birth Name: {data.birthName}</p>
            </>
            <hr/>
          </>
        ))}
      </div>
    </div>
  );
}
