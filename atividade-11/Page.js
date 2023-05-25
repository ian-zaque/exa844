"use client"; 

import Image from 'next/image'
import styles from './page.module.css'
import React from 'react';
import { useState } from 'react';


//Coloque o código dos demais componentes aqui...

export default function Home() {
    
  const [blogMessages, setBlogMessages] = useState([]);
  
  fetch('https://script.googleusercontent.com/macros/echo?user_content_key=Odre_zJAHHW59_psEUdGYiyf9Dm2h2c5Iuu8wsd__YeU1pRFL1WbGhu87iUuxyqLdQH5YzerDCQReVZQxUqH5TqY5xuG5_vgm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnNCc3UlVVUEJX1mktmLCd34_SPokbYEm6BJESWXEp7ZKJL7Uxt4YCwsLwsKWg8EH6Ym9t6fgXKcBlAP9zjCzIuYr92xY2NUROg&lib=Mc7gKNDFWsXKUX18VxT19L_g9uKiEqo84')
    .then(response => response.json())
    .then(data => {
        setBlogMessages(data);
    });
    
    return (
      <main className={styles.main}>
        <FilterableMessageTable messages={blogMessages} />
      </main>
    )
}