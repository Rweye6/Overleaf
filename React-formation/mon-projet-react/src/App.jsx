import { useState } from "react";

const App =() => {
    const [count, setCount] = useState(0);
    return (
        //<div> ici mettre dans une div marche mais pose des imbrications inutiles donc on utilise des balises "vides" : fragments 
        <> //le fameux fragment, c'est pour pouvoir mettre plusieurs éléments différents ici un H1 et un button
            <h1 className="titre">Compteur {count}</h1> //on utilise className à la place de "class" en jsx
            <button onClick={()=>setCount(count +1)}>+</button>
        </>
        //</div>
    );
}

//export default App;


const Bpp=() =>{
    const prenom = 'Alice';
    const age = 27;
    const saluer = (nom) => `Bonjour, $(nom)!`
    
    return (<>
        <p>{prenom}</p>{/*Cette variable est un string */} //acolade pour écrire du javascript
        <p>{age}</p>
        <p>{saluer(prenom)}</p>
    </>
    )
}

//Utilisation de style en ligne en React
function Cpp() {

    const styleBoite = {
        backgroundColor: '#282c34',
        color: 'white',
        borderRadius: '8px'

    }
    return (<>
        <h1 className="mon-titre">Titre</h1>
        <div style = {{color : 'red', fontSize: '20px'}}>Style direct inline</div>
        <div style={styleBoite}>Style via une variable</div>
    </>)
}

//Utilisation de logique en jsx
//jsx n'accepte que des expressions dans les accolades et pas des instructions (conditions)

function Dpp(){
    const estConnecte = true;
    const langages =["Javascript","Python","C"];
    return(
        <>
            <p>{estConnecte ? 'Bienvenue !' : 'Veuillez vous connecter.'}</p> // dans cette formulation on a une constante dont on verifie le true or false  et pas un test logique avec if/else

            <ul>
                {langages.map((langage, index) => (
                    <li key={index}>{index}. {langage}</li>
                )
                )} // le variable.map permet de lister les éléments de langages, on fait donc une fonction fléchée qui affiche chaque élément successivement dans un li
                // Le problème c'est que ca crée une erreur de "clé" qui peut être résolue avec le key dans la liste
            </ul>
        </>
    )
}


// Les props (properties)
//const Carte = (props) =>{
//    console.log(props);
//    return <p>{props.prenom} - {props.age} ans - {props.estAdmin ? 'Administrateur' : 'Membre' } </p>
//}
//const Epp = () =>{
//    return (
//        <>
//            <Carte prenom="Alice" age={28} estAdmin={true} />
//            <Carte prenom="Bob" age={35} estAdmin={true} />
//        </>
//    )
//}


//on fait la même chose en destructurant props
/*const Carte = (props) =>{
    const {prenom, age, estAdmin} = props;
    
    return <p>{prenom} - {age} ans - {estAdmin ? 'Administrateur' : 'Membre' } </p>
}
const Epp = () =>{
    return (
        <>
            <Carte prenom="Alice" age={28} estAdmin={true} />
            <Carte prenom="Bob" age={35} estAdmin={true} />
        </>
    )
}*/

//version finale en destructurant dès le début 

const Carte = ({prenom, age, estAdmin}) =>{
    <><p>{prenom} - {age} ans - {estAdmin ? 'Administrateur' : 'Membre' } </p></>
};
const Epp = () =>{
    return (
        <>
            <Carte prenom="Alice" age={28} estAdmin={true} />
            <Carte prenom="Bob" age={35} estAdmin={true} />
        </>
    )
};

export default Epp;