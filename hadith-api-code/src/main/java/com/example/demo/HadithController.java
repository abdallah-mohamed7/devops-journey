package com.example.demo;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class HadithController {

    private final HadithService hadithService;

    public HadithController(HadithService hadithService) {
        this.hadithService = hadithService;
    }

    @GetMapping("/hadith")
    public Map<String, Object> getDailyHadith() {
        return hadithService.getDailyHadith();
    }
}
