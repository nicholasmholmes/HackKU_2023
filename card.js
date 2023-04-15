class Card {
    constructor(suit, rank, x, y, width, height, color) {
      this.suit = suit;
      this.rank = rank;
      this.x = x;
      this.y = y;
      this.width = width;
      this.height = height;
      this.color = color;
      this.id = null;
      this.dragging = false;
      this.start_x = 0;
      this.start_y = 0;
      this.throttle = 1000 / 60; // 60 fps
      this.lastUpdate = 0;
    }
  
    createCardElement(parentElement) {
      this.id = document.createElement("div");
      this.id.style.width = this.width + "px";
      this.id.style.height = this.height + "px";
      this.id.style.position = "absolute";
      this.id.style.left = this.x + "px";
      this.id.style.top = this.y + "px";
      this.id.style.backgroundColor = this.color;
      this.id.style.borderRadius = "5px";
      this.id.style.border = "1px solid #000";
      this.id.style.textAlign = "center";
      this.id.style.verticalAlign = "middle";
      this.id.style.lineHeight = this.height + "px";
      this.id.innerText = `${this.rank} of ${this.suit}`;
      this.id.addEventListener("mousedown", this.startDrag.bind(this));
      this.id.addEventListener("mouseup", this.stopDrag.bind(this));
      parentElement.appendChild(this.id);
    }
  
    startDrag(event) {
      this.dragging = true;
      this.start_x = event.clientX;
      this.start_y = event.clientY;
    }
  
    stopDrag(event) {
      this.dragging = false;
    }
  
    onDrag(event) {
        if (this.dragging) {
          const now = performance.now();
          if (now - this.lastUpdate > this.throttle) {
            const dx = (event.clientX - this.start_x) / 20; // divide by 20 instead of 10
            const dy = (event.clientY - this.start_y) / 20; // divide by 20 instead of 10
            const new_x = this.x + dx;
            const new_y = this.y + dy;
            const container = this.id.parentElement;
            const container_rect = container.getBoundingClientRect();
            const card_rect = this.id.getBoundingClientRect();
            if (new_x >= container_rect.left && new_x + card_rect.width <= container_rect.right) {
              this.x = new_x;
              this.id.style.left = this.x + "px";
            }
            if (new_y >= container_rect.top && new_y + card_rect.height <= container_rect.bottom) {
              this.y = new_y;
              this.id.style.top = this.y + "px";
            }
            this.start_x = event.clientX;
            this.start_y = event.clientY;
            this.lastUpdate = now;
          }
        }
      }
  }
  