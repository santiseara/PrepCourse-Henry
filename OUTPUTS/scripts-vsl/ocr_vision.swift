import Foundation
import Vision
import AppKit

// Lee rutas de imagenes por stdin (una por linea) y escribe "ruta<TAB>texto" por stdout.
while let line = readLine() {
    let path = line.trimmingCharacters(in: .whitespacesAndNewlines)
    if path.isEmpty { continue }
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print("\(path)\tERR"); continue
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    var out: [String] = []
    do {
        try handler.perform([req])
        for obs in (req.results ?? []) {
            guard let top = obs.topCandidates(1).first else { continue }
            if top.confidence < 0.35 { continue }
            let s = top.string.trimmingCharacters(in: .whitespacesAndNewlines)
            if s.count < 3 { continue }
            out.append(s)
        }
    } catch { out = ["ERR"] }
    print("\(path)\t\(out.joined(separator: " | "))")
    fflush(stdout)
}
