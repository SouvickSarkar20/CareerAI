import { extractResumeData } from "../services/aiExtractor.js";
import axios from "axios";
import fs from "fs";

export const handleResumeUpload = async (req, res) => {
  try {
    const filePath = req.file.path;
    
    // 1. Extract fields from resume using AI/NLP
    const extractedData = await extractResumeData(filePath);

    // 2. Send extracted data to Python ML API for prediction
    const predictionRes = await axios.post("http://127.0.0.1:5000/predict-placement", extractedData);
    const salaryRes = await axios.post("http://127.0.0.1:5000/predict-salary", extractedData);

    // 3. Cleanup file
    fs.unlinkSync(filePath);

    // 4. Return everything to frontend
    res.json({
      extractedData,
      placementPrediction: predictionRes.data,
      salaryPrediction: salaryRes.data
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Something went wrong" });
  }
};
