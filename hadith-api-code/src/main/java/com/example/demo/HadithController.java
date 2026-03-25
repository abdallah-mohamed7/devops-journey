package com.example.demo;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*") // This allows your HTML file to talk to this Java app
public class HadithController {

    private final HadithService hadithService;

    // Spring automatically "injects" the service here
    public HadithController(HadithService hadithService) {
        this.hadithService = hadithService;
    }

    @GetMapping("/hadith")
    public String getDailyHadith() {
        return hadithService.getRamadanHadith();
    }
}