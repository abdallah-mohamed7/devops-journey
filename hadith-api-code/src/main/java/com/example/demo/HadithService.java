package com.example.demo;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.annotation.PostConstruct;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import java.io.InputStream;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;

@Service
public class HadithService {

    private List<Map<String, Object>> hadiths;

    @PostConstruct
    public void init() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        InputStream is = new ClassPathResource("short_bukhari.json").getInputStream();
        hadiths = mapper.readValue(is, new TypeReference<List<Map<String, Object>>>() {});
        System.out.println("Successfully loaded " + hadiths.size() + " hadiths into memory.");
    }

    public Map<String, Object> getDailyHadith() {
        int dayOfYear = LocalDate.now().getDayOfYear();
        return hadiths.get(dayOfYear % hadiths.size());
    }
}
