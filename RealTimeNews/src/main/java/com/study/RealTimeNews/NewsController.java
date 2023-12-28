package com.study.RealTimeNews;

import java.io.IOException;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

@RestController
public class NewsController {
	
	// 클라이언트 구독을 위한 SseEmitter를 저장하는 리스트
	public List<SseEmitter> emitters = new CopyOnWriteArrayList<>();
	
	/**
	 * 클라이언트 구독을 위한 메서드.
	 * 
	 * @return SseEmitter - 클라이언트 통신을 위한 Server-Sent Events emitter.
	 */
	@CrossOrigin
	@RequestMapping(value = "/subscribe", consumes = MediaType.ALL_VALUE)
	public SseEmitter subscribe() {
		// 최대 타임아웃 기간을 가진 새로운 SseEmitter 생성
		SseEmitter sseEmitter = new SseEmitter(Long.MAX_VALUE);
		try {
			// 구독 시 클라이언트에게 초기 데이터 전송
			sseEmitter.send(SseEmitter.event().name("INIT").data("Initial data"));
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		// 완료 콜백 등록하여 emitter를 활성 리스트에서 제거
		sseEmitter.onCompletion(() -> emitters.remove(sseEmitter));
		
		// 새로운 emitter를 활성 리스트에 추가
		emitters.add(sseEmitter);

		// 클라이언트 통신을 위한 emitter 반환
		return sseEmitter;
	}
	
	/**
	 * 모든 구독 중인 클라이언트에게 이벤트를 전송하는 메서드.
	 * 
	 * @param freshNews - 클라이언트에게 전송할 뉴스 데이터.
	 */
	@PostMapping(value = "dispatchEvent")
	public void dispatchEventToClients(@RequestParam String freashNews) {
		// 모든 활성 emitter를 반복하며 최신 뉴스 이벤트 전송
		for(SseEmitter emitter : emitters) {
			try {
				emitter.send(SseEmitter.event().name("latestNews").data(freashNews));
			}catch (IOException e) {
				emitters.remove(emitter);
			}			
		}
		
	}
	
	
}
