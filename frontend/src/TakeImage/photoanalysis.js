import axios from "axios"
import { useState, useEffect, useRef, useCallback } from "react"
import { Link, Navigate, useNavigate } from "react-router-dom"
import { useParams } from "react-router-dom";

const URI = 'http://192.168.0.8:9000/'

const CompAnalizePhoto = () => {
    const [selectedPhoto, setSelectedPhoto] = useState(null);
    const [resultado, setResultado] = useState('')

    const handleFileInputChange = (event) => {
        const file = event.target.files[0];
        setSelectedPhoto(file)
    };

    const handleUploadPhoto = () => {
        if (selectedPhoto) {
            const reader = new FileReader();
            reader.readAsDataURL(selectedPhoto);

            reader.onload = async () => {
                const base64Image = reader.result.split(',')[1]; // Obtener la cadena Base64 sin el prefijo 'data:image/png;base64,'

                try {
                    const response = await axios.post(URI, { image: base64Image });
                    // alert(response.data.message)
                    setResultado('Resultado: ' + response.data.message)
                } catch (error) {
                    console.error(error);
                    alert("Error del servidor: " + error)
                }
            };
        }
    };
    
    return (
        <div>
            <h1>Visual Voice</h1>
            <p>
                Tome una fotografía para su análisis.
            </p>
            <br></br>
            <input type="file" onChange={handleFileInputChange} />
            <button onClick={handleUploadPhoto}>Analizar archivo</button>
            <div style={{marginTop: '30px'}}></div>
            {
                selectedPhoto && 
                (
                    <div>
                        <h2>Archivo seleccionado</h2>
                        <img height='270px' src={URL.createObjectURL(selectedPhoto)} alt="Selected" />
                    </div>
                )
            }

            <h3>
                {resultado}
            </h3>
        </div>
    );
};

export default CompAnalizePhoto;
