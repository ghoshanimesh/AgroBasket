import React, {useEffect} from "react"
import SEO from "../components/seo"

const IndexPage = () => {
  useEffect(() => {
	   navigate("/loginPage");
	}, []);
  return (
  	<div>
   	 <SEO title="Home" />
 	  </div>
  )
}

export default IndexPage
