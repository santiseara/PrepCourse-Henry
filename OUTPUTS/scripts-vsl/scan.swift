import Foundation
import Vision
import AppKit

// Lee rutas de imagenes por stdin (una por linea).
// Escribe: ruta<TAB>FACES=n<TAB>texto1||texto2||...
while let line = readLine() {
    let path = line.trimmingCharacters(in: .whitespacesAndNewlines)
    if path.isEmpty { continue }
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print("\(path)\tERR\t"); fflush(stdout); continue
    }
    let tr = VNRecognizeTextRequest()
    tr.recognitionLevel = .accurate
    tr.usesLanguageCorrection = false
    let fr = VNDetectFaceRectanglesRequest()
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    var out: [String] = []
    var faces = 0
    do {
        try handler.perform([tr, fr])
        for obs in (tr.results ?? []) {
            guard let top = obs.topCandidates(1).first else { continue }
            if top.confidence < 0.35 { continue }
            let s = top.string.trimmingCharacters(in: .whitespacesAndNewlines)
            if s.count < 3 { continue }
            out.append(s)
        }
        // solo caras de tamano real: una cara de fondo minuscula no descalifica el plano
        for f in (fr.results ?? []) {
            if f.boundingBox.width > 0.06 && f.boundingBox.height > 0.06 { faces += 1 }
        }
    } catch {
        print("\(path)\tERR\t"); fflush(stdout); continue
    }
    print("\(path)\tFACES=\(faces)\t\(out.joined(separator: "||"))")
    fflush(stdout)
}
