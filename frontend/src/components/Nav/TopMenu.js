import React from "react";
import styles from "./topMenu.module.scss";
import { Link } from "react-router-dom";

export default function TopMenu() {
  return (
    <React.Fragment>
      <div className={styles.wrapper}>
        <nav>
          <Link to={"/"} style={{ textDecoration: "none" }}>
            <span className={styles.ld}>
              <b>HIP</b>HOP{" "}
            </span>
          </Link>
          <Link to={"/Records"} style={{ textDecoration: "none" }}>
            <span className={styles.btnbox}>Records</span>
          </Link>
          <Link to={"/Artists"} style={{ textDecoration: "none" }}>
            <span className={styles.btnbox}>Artists </span>
          </Link>
          <Link to={"/"} style={{ textDecoration: "none" }}>
            <span className={styles.btnbox}>Home</span>
          </Link>
        </nav>
      </div>
    </React.Fragment>
  );
}
