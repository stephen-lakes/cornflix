function getMovies(){

}

function getColor() {
    let vote = Number(document.getElementsByTagName('span').innerHtml);
    console.log(vote);
    if (vote_average > 7) {
        vote.className = 'green';
    }else if (vote_average > 5) {
        vote.className = 'orange';
    }else {
        vote.className = 'red';
    }

}

/*
form.addEventListener('submit', e=>{
    e.preventDefault();
    const searchItem = search.value;
    if (search) {
        getMovies();
    }
    else {
        getMovies(API_URL)
    }
})*/