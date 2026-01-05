function scrollToSection(){document.getElementById("about").scrollIntoView({behavior:"smooth"})}
const facts=["The fastest airplane reached over 7,000 km/h.","The largest airplane ever built is the Antonov An-225.","Commercial planes fly over 10,000 meters high.","Airplane wings create lift using air pressure.","Black boxes are actually orange."]
function newFact(){const r=Math.floor(Math.random()*facts.length);document.getElementById("fact").textContent=facts[r]}
