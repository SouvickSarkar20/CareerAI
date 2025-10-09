import express from "express";
import multer from "multer";
import { handleResumeUpload } from "../controllers/resumeController.js";

const router = express.Router();
const upload = multer({ dest: "uploads/" });  // stores file in /uploads

router.post("/upload", upload.single("resume"), handleResumeUpload);

export default router;
