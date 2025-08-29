const playBoard = document.querySelector(".play-board");
        const scoreElement = document.querySelector(".score");
        const highScoreElement = document.querySelector(".high-score");

        let gameOver = false
        let foodX, foodY;
        let snakeX = 5, snakeY = 10;
        let snakeBody = []; //partes del cuerpo de la serpiente
        let velocityX = 0, velocityY = 0;
        let setIntervalId;
        let score = 0;

        // Usando variable en memoria en lugar de localStorage
        let highScore = localStorage.getItem("high-score") || 0;
        highScoreElement.innerHTML = `High Score: ${highScore}`;

        // posicion aleatoria de manzanas
        const changeFoodPosition = () => {
            foodX = Math.floor(Math.random() * 30) + 1;
            foodY = Math.floor(Math.random() * 30) + 1;
        }

        const handleGameOver = () => {
            clearInterval(setIntervalId);
            alert("Game Over");
            location.reload();
        }

        // controles
        const changeDirection = (e)=> {
            if(e.key === "ArrowUp" && velocityY != 1) {
                velocityX = 0;
                velocityY = -1;
            } else if(e.key === "ArrowDown" && velocityY != -1) {
                velocityX = 0;
                velocityY = 1;
            } else if(e.key === "ArrowLeft" && velocityX != 1) {
                velocityX = -1;
                velocityY = 0;
            } else if(e.key === "ArrowRight" && velocityX != -1) {
                velocityX = 1;
                velocityY = 0;
            } 
        }

        const initGame = () => {
            if(gameOver) return handleGameOver();
            let htmlMarkup = `<div class="food" style="grid-area: ${foodY} / ${foodX}"></div>`;
            
            if(snakeX === foodX && snakeY === foodY) {
                changeFoodPosition();
                snakeBody.push([foodX, foodY]);
                score++;

                highScore = score >= highScore ? score : highScore; //almacenamiento de puntaje maximo
                localStorage.setItem("high-score", highScore);
                scoreElement.innerHTML = `Score: ${score}`;
                highScoreElement.innerHTML = `high Score: ${highScore}`;
            }
            
            for(let i = snakeBody.length -1; i > 0; i--) {
                snakeBody[i] = snakeBody[i - 1];
            }

            snakeBody[0] = [snakeX, snakeY];

            snakeX += velocityX;
            snakeY += velocityY;

            if(snakeX <= 0 || snakeX > 30 || snakeY <= 0 || snakeY > 30) {
                gameOver = true;
            }

            for(let i = 0 ; i < snakeBody.length; i++){
                // La cabeza (primer elemento) tiene clase "head", el resto "body"
                const segmentClass = i === 0 ? "head" : "body";
                htmlMarkup += `<div class="${segmentClass}" style="grid-area: ${snakeBody[i][1]} / ${snakeBody[i][0]}"></div>`;
                
                //muerte consigo mismo
                if(i !== 0 && snakeBody[0][1] === snakeBody[i][1] && snakeBody[0][0] === snakeBody[i][0]) {
                    gameOver = true;
                }
            }
            playBoard.innerHTML = htmlMarkup;
        }

        changeFoodPosition();
        setIntervalId = setInterval(initGame, 125);
        document.addEventListener("keydown", changeDirection);