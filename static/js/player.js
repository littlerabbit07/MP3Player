const audio = document.getElementById('audio');
const tracks = document.querySelectorAll('.track');
const currentTrackEl = document.getElementById('current-track');
let currentIndex = 0;

// Load a track
function loadTrack(index) {
    const track = tracks[index];
    audio.src = track.dataset.src;
    currentTrackEl.textContent = '▶️ ' + track.textContent;
    audio.play();
}

// Click track in playlist
tracks.forEach((track, index) => {
    track.addEventListener('click', () => {
        currentIndex = index;
        loadTrack(currentIndex);
    });
});

// Controls
document.getElementById('play').addEventListener('click', () => audio.play());
document.getElementById('pause').addEventListener('click', () => audio.pause());

document.getElementById('prev').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + tracks.length) % tracks.length;
    loadTrack(currentIndex);
});

document.getElementById('next').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % tracks.length;
    loadTrack(currentIndex);
});

// Search filter
document.getElementById('search').addEventListener('input', function() {
    const term = this.value.toLowerCase();
    tracks.forEach(track => {
        if (track.textContent.toLowerCase().includes(term)) {
            track.style.display = '';
        } else {
            track.style.display = 'none';
        }
    });
});
