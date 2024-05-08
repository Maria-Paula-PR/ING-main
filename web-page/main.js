// Función para grabar audio
function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function (stream) {
            recorder = new MediaRecorder(stream);
            chunks = [];

            recorder.ondataavailable = function (e) {
                chunks.push(e.data);
            };

            recorder.onstop = async function (e) {
                var blob = new Blob(chunks, { 'type': 'audio/ogg; codecs=opus' });
                var audioURL = window.URL.createObjectURL(blob);
                recordedAudio.src = audioURL;
                recordedAudio.blob = blob;
            
                const audioBuffer = recordedAudio.blob.arrayBuffer().then(buff => buff);

                const formData = new FormData();
                formData.append('audio', blob, "audio.ogg");

                await fetch('http://localhost:5555/process_audio', {
                    method: 'POST',
                    mode: "no-cors",
                    headers: {"access-control-allow-origin": "*"},
                    body: formData,
                }).then(response => response.json())
                .then(data => resolve(data))
                .catch(error => console.error('Error:', error));
                
                console.log('Audio enviado');
                
                chunks = [];
            };

            recorder.start();
            stopRecordingBtn.disabled = false;
            startRecordingBtn.disabled = true;
        })
        .catch(function (err) {
            console.log('Error al acceder al dispositivo de audio: ', err);
        });
}

// Función para detener la grabación
function stopRecording() {
    recorder.stop();
    stopRecordingBtn.disabled = true;
    startRecordingBtn.disabled = false;
}

// Obtenemos los botones
var startRecordingBtn = document.getElementById('startRecording');
var stopRecordingBtn = document.getElementById('stopRecording');
var recordedAudio = document.getElementById('recordedAudio');

// Variable para el objeto MediaRecorder
var recorder;
// Variable para almacenar los fragmentos de audio grabados
var chunks = [];

// Event listener para comenzar la grabación
startRecordingBtn.addEventListener('click', startRecording);

// Event listener para detener la grabación
stopRecordingBtn.addEventListener('click', stopRecording);