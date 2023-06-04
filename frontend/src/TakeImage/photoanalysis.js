import axios from "axios"
import { useState, useEffect, useRef, useCallback } from "react"
import { Link, Navigate, useNavigate } from "react-router-dom"
import { useParams } from "react-router-dom";

const CompAnalizePhoto = () => {
  const [selectedPhoto, setSelectedPhoto] = useState(null);

  const handleFileInputChange = (event) => {
    const file = event.target.files[0];
    setSelectedPhoto(file);
  };

  const handleUploadPhoto = () => {
    if (selectedPhoto) {
      console.log('sigue la foto')
      console.log(selectedPhoto);

      const reader = new FileReader();
      reader.readAsDataURL(selectedPhoto);
      reader.onload = async () => {
        const base64Image = reader.result.split(',')[1]; // Obtén la cadena Base64 sin el prefijo 'data:image/png;base64,'
 
        console.log('base64')
        console.log(base64Image)

        try {
          const response = await axios.post('http://127.0.0.1:9000/', { image: base64Image });
          console.log(response.data); // Respuesta del servidor
        } catch (error) {
          console.error(error);
        }
      };
    }
  };
  

  return (
    <div>
      <h1>Tome una fotografía para su análisis</h1>
      <input type="file" onChange={handleFileInputChange} />
      <button onClick={handleUploadPhoto}>Analizar archivo</button>
      <div style={{marginTop: '50px'}}></div>
      {
        selectedPhoto && 
        (
            <div>
                <h2>Archivo seleccionado</h2>
                <img height='300px' src={URL.createObjectURL(selectedPhoto)} alt="Selected" />
            </div>
        )
      }
    </div>
  );
};

export default CompAnalizePhoto;
