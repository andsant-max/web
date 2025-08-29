            let logo = document.getElementById("logo")
            let burro = document.getElementById("burro");
            let burros = document.getElementById("burros");
            let taco = document.getElementById("taco");
            let tacos = document.getElementById("tacos");

            window.addEventListener("scroll", function(){
                let value = window.scrollY;
                logo.style.top = value * 0.25+'px';
                burro.style.top = value * -0.5+'px';
                burros.style.top = value * -2+'px';
                taco.style.top = value * -0.25+'px';
                tacos.style.top = value * -0.75+'px';

            })