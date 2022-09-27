import React, { useEffect, useState } from "react";
import styles from "./home.module.scss";

export default function Home() {
  const [hiphopData, setHiphopData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/hiphop")
      .then((response) => response.json())
      .then((data) => {
        setHiphopData(data);
      });
  }, []);

  return (
    <div className={styles.wrapper}>
      <div className={styles.content}>
        {hiphopData.map((data) => (
          <>
            <>
              <img alt="" src={data.thumbnail} />
              <div class="text">
                <p>{data.abstract}</p>
              </div>
              <p>
                Instruments:{" "}
                {data.instruments.map((instrument) => (
                  <a href={instrument}>
                    {instrument}
                    <br />
                  </a>
                ))}
              </p>
            </>
            <hr />
          </>
        ))}
      </div>
    </div>
  );
}
